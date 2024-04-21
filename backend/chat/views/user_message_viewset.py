"""
Module containing the UserMessage views.
"""

from rest_framework import permissions, viewsets

from chat.models import UserMessage
from chat.serializers import UserMessageSerializer


class UserMessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint to define UserMessage actions.

    The available actions for the UserMessages model are:
    * List
    * Create
    * Retrieve
    * Update
    * Destroy
    """

    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
    permission_classes = [permissions.AllowAny]
    # permission_classes = [permissions.IsAuthenticated]
