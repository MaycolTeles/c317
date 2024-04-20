"""
Module containing the DefaultSerializer class.
"""

from rest_framework import serializers


class DefaultSerializer(serializers.ModelSerializer):
    """
    """
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        abstract = True
        fields = "__all__"
