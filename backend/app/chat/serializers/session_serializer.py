
from rest_framework import serializers

from account.models import User
from chat.models import Session
from core.mixins import DefaultSerializer


class SessionSerializer(DefaultSerializer):
    """
    """

    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=User.objects.all())
    helpful_score = serializers.IntegerField(required=False)

    class Meta:
        model = Session
        fields = "__all__"
