from http import HTTPStatus

from django.contrib.auth import authenticate
from django.test import TestCase
from django.urls import reverse_lazy

from tests.mixins import TestWithUsersMixin


class TestClientLoginView(TestWithUsersMixin, TestCase):
    def test_get(self):
        request = self.client.get(reverse_lazy('login'))
        self.assertEqual(request, HTTPStatus.OK)

    def test_post(self):
        request = self.client.post(
            reverse_lazy('login'),
            data={
                'username': self.test_client1.username,
                'password': self.test_client1.password,
            },
        )

        self.assertEqual(request.status_code, HTTPStatus.OK)
        self.assertTrue(self.test_client1.is_authenticated)


class TestSignUpView(TestWithUsersMixin, TestCase):

    def test_get(self):
        request = self.client.get(reverse_lazy('signup'))
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_post(self):
        request = self.client.post(
            reverse_lazy('signup'),
            data=self.test_client1.clean(),
        )
        self.assertEqual(request.status_code, HTTPStatus.OK)
        self.assertTrue(self.test_client1.is_authenticated)


class ResetPasswordView(TestWithUsersMixin, TestCase):

    def test_get(self):
        request = self.client.get(reverse_lazy('reset'))
        self.assertEqual(request.status_code, HTTPStatus.OK)

    def test_post(self):
        request = self.client.post(
            reverse_lazy('reset'),
            data={'email': self.test_client1.email},
        )
        self.assertEqual(request.status_code, HTTPStatus.FOUND)


class TestLogoutView(TestWithUsersMixin, TestCase):

    def test_get(self):
        authenticate(username='TestClient1', password='testpassword1')
        request = self.client.get(reverse_lazy('logout'))
        self.assertEqual(request.status_code, HTTPStatus.FOUND)

        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
