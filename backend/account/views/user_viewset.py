"""
Module containing the User views.
"""

from rest_framework import permissions, viewsets

from account.models import User
from account.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to define User actions.

    The available actions for the User model are:
    * List
    * Create
    * Retrieve
    * Update
    * Destroy
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
