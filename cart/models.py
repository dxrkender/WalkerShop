"""Creating a `Category` and `Product` models."""
from django.db import models
from django.utils import timezone

from account.models import Client


class ProductCategory(models.Model):
    """Implementing model category of products."""

    _default_field_short_length: int = 127

    category_name = models.CharField(
        max_length=_default_field_short_length,
    )

    def __str__(self):
        """Magic method for print instance.

        Returns:
            String representation of an object instance.
        """
        return '<ProductCategory: {name}>'.format(name='self.category_name')


class Product(models.Model):
    """Implementing model product."""

    _default_field_length: int = 255

    product_name = models.CharField(
        verbose_name='Product',
        max_length=_default_field_length,
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
        on_delete=models.PROTECT,
    )

    cart_id = models.ManyToManyField(
        to=Client,
        related_name='user_cart',
        db_table='cart',
    )

    def __str__(self):
        """Magic method for print instance.

        Returns:
            String representation of an object instance.
        """
        return '<Product: {name} - {price}>'.format(
            name=self.product_name,
            price=self.price,
        )
