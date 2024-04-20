"""
Module containing the User admin.
"""

from django.contrib import admin

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin class for the User model.
    """

    search_fields = ('email', 'name',)
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    exclude = ('password',)
