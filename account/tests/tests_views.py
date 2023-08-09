from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse_lazy

from account.models import Client
from tests.mixins import TestWithUsersMixin


class TestClientLoginView(TestWithUsersMixin, TestCase):
    pass


class TestSignUpView(TestWithUsersMixin, TestCase):
    def test_get(self):
        request = self.client.get(reverse_lazy('signup'))
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_post(self):
        request = self.client.post(
            reverse_lazy('signup'),
            data=self.test_client1.clean()
        )
        self.assertEqual(request.status_code, HTTPStatus.OK)
        self.assertTrue(self.test_client1.is_authenticated)


class TestForgotView(TestWithUsersMixin, TestCase):
    def test_get(self):
        request = self.client.get(reverse_lazy('forgot'))
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_post(self):
        # TODO: you need to write services for this test
        pass


class TestLogoutView(TestWithUsersMixin, TestCase):
    def test_get(self):
        request = self.client.get(reverse_lazy('forgot'))
        self.assertEqual(request.status_code, HTTPStatus.OK)
