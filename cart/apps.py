"""This module adds config for account application."""

from django.apps import AppConfig


class CartConfig(AppConfig):
    """Class representing a Cart application and its configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
