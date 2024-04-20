
from rest_framework import serializers

from chat.models import ChatBotMessage
from chat.serializers.message_serializer import MessageSerializer


class ChatBotMessageSerializer(MessageSerializer):
    """
    """

    helpful_score = serializers.IntegerField()

    class Meta:
        model = ChatBotMessage
        fields = "__all__"
