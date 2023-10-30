import os
from typing import Callable, Any
from unittest import TestCase
from test.support.os_helper import EnvironmentVarGuard

from account.models import Client


class TestWithUsersMixin(TestCase):

    def setUp(self) -> None:

        self.test_client1 = Client.objects.create_user(
            username='TestClient1',
            email='test@client.com',
            password='testpassword1',
            is_active=True,
        )
        self.test_client2 = Client.objects.create_user(
            username='ТестКлиент2',
            email='test2@client.com',
            password='testpassword2',
            is_active=True,
        )
        self.test_client1.save()
        self.test_client2.save()

    def tearDown(self) -> None:
        self.test_client1.delete()
        self.test_client2.delete()
