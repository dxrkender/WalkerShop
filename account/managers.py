"""Temporary module."""
from django.db import models

from account.models import Client


class ClientManager(models.Manager):
    """Temporary class."""

    def get_client_by_email(self, email: str) -> Client:
        """Temporary method.

        Temp.

        Args:
            email (str): temp

        Returns:
            Temp.
        """
        try:
            client = self.objects.get(email=email)
        except self.DoesNotExist:
            client = None
        return client
