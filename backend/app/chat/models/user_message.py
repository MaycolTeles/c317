
from django.db import models

from account.models import User
from chat.models.message import Message


class UserMessage(Message):
    """
    Class to represent a user message.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
