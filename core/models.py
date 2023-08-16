from django.db import models
from django.utils import timezone

from account.models import Client


class ProductCategory(models.Model):
    category_name = models.CharField(
        max_length=128,
    )

    def __str__(self):
        return f'<ProductCategory: {self.category_name}>'


class Product(models.Model):
    product_name = models.CharField(
        verbose_name='Product',
        max_length=256,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Quantity',
    )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=8,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        verbose_name='Start selling from',
        default=timezone.now,
    )
    sales = models.DecimalField(
        verbose_name='Sales',
        max_digits=3,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name='Is active',
    )

    category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'<Product: {self.product_name} - {self.price}>'
