"""
Module containing the Session admin.
"""

from django.contrib import admin

from chat.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """
    Admin class for the Session model.
    """

    list_display = ('user', 'helpful_score')
    list_filter = ('user', 'helpful_score')
    readonly_fields = ('id', 'created_at', 'updated_at')
    fields = ('id', 'created_at', 'updated_at', 'user', 'helpful_score')
