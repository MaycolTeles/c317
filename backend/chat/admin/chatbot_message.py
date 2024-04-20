"""
Module containing the ChatBotMessage admin.
"""

from django.contrib import admin

from chat.models import ChatBotMessage


@admin.register(ChatBotMessage)
class ChatBotMessageAdmin(admin.ModelAdmin):
    """
    Admin class for the ChatBotMessage model.
    """

    list_display = ('session', 'created_at', 'helpful_score')
    list_filter = ('session', 'helpful_score')
    fields = ('id', 'created_at', 'updated_at', 'session', 'helpful_score')

