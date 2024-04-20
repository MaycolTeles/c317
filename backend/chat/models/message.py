
from django.db import models

from chat.models.session import Session
from core.mixins import DefaultModel


class Message(DefaultModel):
    """
    Class to represent a chat message.
    """

    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        abstract = True
