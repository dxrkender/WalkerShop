"""Creating a `Category` and `Product` models."""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from account.models import Client


class ProductSubcategory(models.Model):
    """Implementing model subcategory of category .

    Attributes:
        _default_field_short_length (int):
            It's the constant for `model.CharField`.

        subcategory_name (models.CharField):
            This field is for the name of the clothing category.
    """

    _default_field_short_length: int = 127

    subcategory_name: models.CharField = models.CharField(
        max_length=_default_field_short_length,
    )

    class Meta(AbstractUser.Meta):
        """Metaclass for classes for media model definitions.

        Attributes:
            verbose_name (str):
                A human-readable name for the object, singular.

            verbose_name_plural (str):
                The plural name for the object.

            db_table (str):
                It's the name of the database table.
        """

        db_table = 'product_subcategory'

        verbose_name = 'Product subcategory'
        verbose_name_plural = 'Product subcategories'

    def __repr__(self):
        """Magic method for print instance in console.

        Returns:
            String representation of an object instance.
        """
        return '<ProductSubcategory: {name}>'.format(
            name=self.subcategory_name,
        )

    def __str__(self):
        """Magic method for print instance.

        Returns:
            String representation of an object instance.
        """
        return 'Product Subcategory'


class ProductCategory(models.Model):
    """Implementing model category of products.

    Attributes:
        _default_field_short_length (int):
            It's the constant for length of field.

        _default_field_medium_length (int):
            It's the constant for length of field.

        category_name (models.CharField):
            This field is for the name of the clothing category.

        category_description (models.TextField):
            This field is for description of the category.
    """

    _default_field_short_length: int = 127
    _default_field_medium_length: int = 255

    category_name: models.CharField = models.CharField(
        max_length=_default_field_short_length,
    )

    category_description = models.TextField(
        max_length=_default_field_medium_length,
        default='Category of products',
    )

    subcategory = models.ForeignKey(
        to=ProductSubcategory,
        on_delete=models.PROTECT,
        null=True,
    )

    class Meta(AbstractUser.Meta):
        """Metaclass for classes for media model definitions.

        Attributes:
            verbose_name (str):
                A human-readable name for the object, singular.

            verbose_name_plural (str):
                The plural name for the object.
        """

        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    def __repr__(self):
        """Magic method for print instance in console.

        Returns:
            String representation of an object instance.
        """
        return '<ProductCategory: {name}>'.format(name=self.category_name)

    def __str__(self):
        """Magic method for print instance.

        Returns:
            String representation of an object instance.
        """
        return 'Product Category: {name}'.format(name=self.category_name)


class Product(models.Model):
    """Implementing model product.

    Attributes:
        _default_field_medium_length (int):
            It's the constant for length of field.

        product_name (models.CharField):
            This field is for the name of the clothing product.

        quantity (models.PositiveIntegerField):
            This field is total quantity of the clothing product.

        price (models.DecimalField):
            This field is current price of the clothing product.

        created_at (models.DateTimeField):
            This field indicates the date the product
            was added in the database.

        sales (models.DecimalField):
            This field is current sales of the clothing product.

        is_active (models.BooleanField):
            This field contains information about whether
            the client is active or not.

        category (models.ForeignKey):
            This field is foreign key to the product's subcategory.

        cart_id (models.ManyToManyField):
            This field is many to many key to the user's cart.
    """

    _default_field_medium_length: int = 255

    product_name = models.CharField(
        verbose_name='Product',
        max_length=_default_field_medium_length,
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

    def __repr__(self):
        """Magic method for print instance in console.

        Returns:
            String representation of an object instance.
        """
        return '<Product: {name} - {price}>'.format(
            name=self.product_name,
            price=self.price,
        )

    def __str__(self):
        """Magic method for print instance.

        Returns:
            String representation of an object instance.
        """
        return 'Shop product'


class AudienceCategory(models.Model):
    """Implementing model category of audience.

    Attributes:
        _default_field_short_length (int):
            It's the constant for length of field.

        _default_field_medium_length (int):
            It's the constant for length of field.

        audience_name (models.CharField):
            This field is for the name of the audience.

        audience_description (models.TextField):
            This field is for description of the audience.

        categories (models.ManyToManyField):
            This field is many to many key to the user's category.
    """

    _default_field_short_length: int = 127
    _default_field_medium_length: int = 255

    audience_name = models.CharField(
        max_length=_default_field_short_length,
    )

    audience_description = models.TextField(
        max_length=_default_field_medium_length,
    )

    categories = models.ManyToManyField(
        to=ProductCategory,
        related_name='audience_categories',
    )

    class Meta(AbstractUser.Meta):
        """Metaclass for classes for media model definitions.

        Attributes:
            verbose_name (str):
                A human-readable name for the object, singular.

            verbose_name_plural (str):
                The plural name for the object.
        """

        verbose_name = 'Audience category'
        verbose_name_plural = 'Audience categories'

    def __repr__(self):
        """Magic method for print instance in console.

        Returns:
            String representation of an object instance.
        """
        return '<ClientAudienceCategory: {name}>'.format(
            name='self.audience_name',
        )

    def __str__(self):
        """Magic method for print instance.

        Returns:
            String representation of an object instance.
        """
        return 'Audience Category'
