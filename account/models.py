from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Client(AbstractUser):
    username = models.CharField(
        max_length=256,
        validators=[MinLengthValidator(limit_value=5)],
        unique=True,
        verbose_name='Username',
    )
    email = models.EmailField(
        null=False,
        max_length=256,
        verbose_name='Email',
    )

    slug = models.SlugField(
        verbose_name='Slug',
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Activity',
    )

    date_joined = models.DateTimeField(
        auto_now=True,
        verbose_name='Joined at'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("home", kwargs={'slug_id': self.slug})

    def __str__(self):
        return f'<User: {self.username} - {self.email} - {self.slug}>'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
