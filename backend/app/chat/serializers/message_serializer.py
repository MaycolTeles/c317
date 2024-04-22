
from rest_framework import serializers

from chat.models import Message, Session
from core.mixins import DefaultSerializer


class MessageSerializer(DefaultSerializer):
    """
    """

    session = serializers.PrimaryKeyRelatedField(queryset=Session.objects.all())
    content = serializers.CharField()

    class Meta:
        abstract = True
        model = Message
        fields = "__all__"
