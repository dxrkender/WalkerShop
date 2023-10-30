from django.core.exceptions import ValidationError
from django.test import TestCase
from account.models import Client
from tests.mixins import TestWithUsersMixin


class TestClient(TestWithUsersMixin, TestCase):

    def test_save(self):
        test_client1 = Client.objects.get(pk=self.test_client1.pk)
        self.assertEqual(test_client1.slug, 'testclient1')

    def test_verbose_name(self):
        test_client1 = Client.objects.get(pk=self.test_client1.pk)

        username_verbose_name = test_client1._meta.get_field(
            'username').verbose_name
        email_verbose_name = test_client1._meta.get_field('email').verbose_name
        slug_verbose_name = test_client1._meta.get_field('slug').verbose_name
        is_active_verbose_name = test_client1._meta.get_field(
            'is_active',
        ).verbose_name
        date_joined_verbose_name = test_client1._meta.get_field(
            'date_joined',
        ).verbose_name

        self.assertEqual(username_verbose_name, 'Username')
        self.assertEqual(email_verbose_name, 'Email')
        self.assertEqual(slug_verbose_name, 'Slug')
        self.assertEqual(is_active_verbose_name, 'Activity')
        self.assertEqual(date_joined_verbose_name, 'Joined at')

    def test_str(self):
        test_client1 = Client.objects.get(pk=self.test_client1.pk)
        test_client2 = Client.objects.get(pk=self.test_client2.pk)
        self.assertEqual(
            str(test_client1),
            '<Client: TestClient1 - test@client.com - testclient1>',
        )
        self.assertEqual(
            str(test_client2),
            '<Client: ТестКлиент2 - test2@client.com - 2>',
        )

    def test_username_validators(self):
        self.test_client3 = Client.objects.create_user(
            username='abc',
            email='abc@abc.com',
            is_active=True,
        )
        with self.assertRaises(ValidationError):
            self.test_client3.full_clean()

    def test_get_absolute_username(self):
        test_client1 = Client.objects.get(pk=self.test_client1.pk)
        self.assertEqual('/cart/testclient1/', test_client1.get_absolute_url())
