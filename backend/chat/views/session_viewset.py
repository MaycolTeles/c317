"""
Module containing the Session views.
"""

from rest_framework import permissions, viewsets

from chat.models import Session
from chat.serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint to define Session actions.

    The available actions for the Session model are:
    * List
    * Create
    * Retrieve
    * Update
    * Destroy
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
