import json
from uuid import UUID

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import structlog

from chat.models import Session, UserMessage, ChatBotMessage
from chat.chatbot import ChatBot, CHATBOT_DEFER_MESSAGE


logger = structlog.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    _session_id: str
    _room_group_name: str
    _defer_to_human_support = False
    _chatbot = ChatBot()

    async def connect(self):
        session_id: UUID = self.scope["url_route"]["kwargs"]["session_id"]
        self._session_id = session_id.hex
        self._room_group_name = f"chat_{self._session_id}"

        # Join room group
        await self.channel_layer.group_add(self._room_group_name, self._session_id)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self._room_group_name, self._session_id)

    async def receive(self, text_data):
        """
        Method to receive a message from the WebSocket
        and send it to the room group.
        """
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to ChatBot Assistant
        if not self._defer_to_human_support:
            response = self._chatbot.send_message(message)

            # Save message to database
            await database_sync_to_async(self._create_chatbot_message)(response)

            logger.info(f"response: {response}")

            # Chatbot unable to help the user. Defer to human support.
            if response.find(CHATBOT_DEFER_MESSAGE):
                self._defer_to_human_support = True
                logger.info("Defering to human support...")
                logger.info(f"_session_id: {self._session_id}")
                logger.info(f"group_name: {self._room_group_name}")
                logger.info(f"response: {response}")

        # Chatbot deferred to human support. Send message to WebSocket.
        else:
            logger.info("TESTANDO AQUI")

        # Save user message into database
        await database_sync_to_async(self._create_user_message)(message)

        # Send response to WebSocket
        await self.send(text_data=json.dumps({"message": response}))

        # Send message to room group
        msg = {"type": "chat_message", "message": message}
        await self.channel_layer.group_send(self._room_group_name, msg)

    # async def chat_message(self, event):
    #     """
    #     Method to receive a message from the room group
    #     and send it to the WebSocket.
    #     """
    #     message = event["message"]

    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({"message": message}))

    def _create_user_message(self, message: str):
        """
        Method to create a user message.
        """
        session = Session.objects.get(id=self._session_id)

        UserMessage.objects.create(
            session_id=session.id,
            user=session.user,
            content=message,
        )

    def _create_chatbot_message(self, message: str):
        """
        Method to create a chatbot message.
        """
        ChatBotMessage.objects.create(
            session_id=self._session_id,
            content=message,
        )

    # def _create_support_message(self, message: str):
    #     """
    #     Method to create a support message.
    #     """
    #     SupportMessage.objects.create(
    #         session_id=self._session_id,
    #         content=message,
    #     )
