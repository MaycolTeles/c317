"""
Module containing the DefaultModel class.
"""
import uuid
from django.db import models


class DefaultModel(models.Model):
    """
    Class to add the following fields to all models that inherit from it:

    `id` : `UUIDField`
        To be used as the primary key.

    `created_at` : `DateTimeField`
        To store the date and time of creation.

    `updated_at` : `DateTimeField`
        To store the date and time of the last update.
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)
