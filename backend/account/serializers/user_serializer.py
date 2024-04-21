"""
Module containing the User serializer.
"""

from rest_framework import serializers

from account.models import User
from core.mixins import DefaultSerializer


class UserSerializer(DefaultSerializer):
    """
    Class to serialize the User model.
    """

    email = serializers.EmailField()
    name = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'id',
            'created_at',
            'updated_at',
            'email',
            'name',
        )
