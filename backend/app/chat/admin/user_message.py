"""
Module containing the UserMessage admin.
"""

from django.contrib import admin

from chat.models import UserMessage


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    """
    Admin class for the UserMessage model.
    """

    list_display = ('session', 'user')
    list_filter = ('session', 'user')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fields = ('id', 'created_at', 'updated_at', 'session', 'user', 'content')
