"""
Module containing the User model.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.mixins import DefaultModel


class User(AbstractUser, DefaultModel):
    """
    Class to represent an user.
    """

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)

    REQUIRED_FIELDS = [
        'email',
        'name',
    ]
