"""This module add models in admin UI and customize it."""

from django.contrib import admin

from account.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Customize client model in admin UI."""

    fields = ('username', 'email', 'is_active')
    list_display = ('username', 'email', 'slug', 'is_active', 'date_joined')
