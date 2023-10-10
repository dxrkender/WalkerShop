"""Creating a Client model."""

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# from account.managers import ClientManager  # noqa


class Client(AbstractUser):
    """
    Implementing a fully featured User model with admin-compliant permissions.

    Username, email, slug and password are required.
    """

    _default_field_length: int = 255

    class Meta(AbstractUser.Meta):
        """Metaclass for classes for media model definitions."""

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    username: models.CharField = models.CharField(
        max_length=_default_field_length,
        validators=[MinLengthValidator(limit_value=5)],
        unique=True,
        verbose_name='Username',
    )
    email: models.EmailField = models.EmailField(
        null=False,
        max_length=_default_field_length,
        verbose_name='Email',
    )

    slug: models.SlugField = models.SlugField(
        verbose_name='Slug',
        unique=True,
        null=False,
    )

    is_active: models.BooleanField = models.BooleanField(
        default=True,
        verbose_name='Activity',
    )

    date_joined: models.DateTimeField = models.DateTimeField(
        auto_now=True,
        verbose_name='Joined at',
    )

    # client_manager: models.Manager = ClientManager()  # noqa

    def save(self, *args, **kwargs) -> None:
        """Adding a slug to a client object during the initial save process.

        Args:
            args (Any): Passing args to the parent's constructor.
            kwargs (Any): Passing args to the parent's constructor.
        """
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Create url from client's slug.

        Returns:
            Retrieving url details from the urls.py file through the viewname
            value provided.
        """
        return reverse(viewname='home', kwargs={'slug_id': self.slug})

    def __str__(self):
        """Magic method for print instance.

        Returns:
            String representation of an object instance.
        """
        return '<Client: {username} - {email} - {slug}>'.format(
            username=self.username,
            email=self.email,
            slug=self.slug,
        )
