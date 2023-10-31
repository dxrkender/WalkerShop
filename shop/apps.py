"""This module adds config for account application."""

from django.apps import AppConfig


class ShopConfig(AppConfig):
    """Class representing a Shop application and its configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
