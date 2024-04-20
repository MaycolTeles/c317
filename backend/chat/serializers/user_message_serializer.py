
from rest_framework import serializers

from account.models import User
from chat.models import UserMessage
from chat.serializers.message_serializer import MessageSerializer


class UserMessageSerializer(MessageSerializer):
    """
    """

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserMessage
        fields = "__all__"
