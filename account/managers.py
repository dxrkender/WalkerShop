from typing import Optional

from django.db import models


class ClientManager(models.Manager):

    def get_client_by_email(self, email: str):
        try:
            client = self.objects.get(email=email)
        except self.DoesNotExist:
            client = None
        return client
