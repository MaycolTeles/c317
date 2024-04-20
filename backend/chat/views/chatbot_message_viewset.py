"""
Module containing the ChatBotMessage views.
"""

from rest_framework import permissions, viewsets

from chat.models import ChatBotMessage
from chat.serializers import ChatBotMessageSerializer


class ChatBotMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint to define ChatBotMessage actions.

    The available actions for the ChatBotMessages model are:
    * List
    * Create
    * Retrieve
    * Update
    * Destroy
    """

    queryset = ChatBotMessage.objects.all()
    serializer_class = ChatBotMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
