
from rest_framework import serializers

from account.models import User
from chat.models import Session
from core.mixins import DefaultSerializer


class SessionSerializer(DefaultSerializer):
    """
    """

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    helpful_score = serializers.IntegerField()

    class Meta:
        model = Session
        fields = "__all__"