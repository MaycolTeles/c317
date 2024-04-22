
from django.db import models

from account.models import User
from core.mixins import DefaultModel


class Session(DefaultModel):
    """
    Class to represent a chat session.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    helpful_score = models.IntegerField(default=0)
