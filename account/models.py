from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Client(AbstractUser):
    username = models.CharField(max_length=256, validators=[MinLengthValidator(5)], unique=True)
    email = models.EmailField(null=False, max_length=256)

    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("account", kwargs={'slug': self.slug})

    def __str__(self):
        return f'<User: {self.username} - {self.email} - {self.slug}>'
