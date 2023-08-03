from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Client(AbstractBaseUser):
    username = models.CharField(max_length=256, validators=[MinLengthValidator(5)])
    email = models.EmailField(null=False, max_length=256)

    slug = models.SlugField()
    password = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(self.username)
