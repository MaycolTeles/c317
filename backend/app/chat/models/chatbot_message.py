
from django.db import models

from chat.models.message import Message


class ChatBotMessage(Message):
    """
    Class to represent a chatbot message.
    """

    helpful_score = models.IntegerField(default=0)
