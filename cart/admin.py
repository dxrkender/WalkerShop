"""Module for customizing admin interface for this application."""
from typing import Tuple

from django.contrib import admin

from cart.models import Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """Customizing admin interface for `ProductCategory` model.

    Attributes:
        fields (Tuple[str]): Fields of model instance which
            will be able to add or change in forms.

        list_display (Tuple[str]):
            Fields which will be displayed admin interface.
    """

    fields: Tuple[str] = ('category_name',)
    list_display: Tuple[str] = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Customizing admin interface for `ProductAdmin` model.

    Attributes:
        fields (Tuple[str]): Fields of model instance which
            will be able to add or change in forms.

        list_display (Tuple[str]):
            Fields which will be displayed admin interface.
    """

    fields: Tuple[str] = (
        'product_name',
        'quantity',
        'price',
        'created_at',
        'sales',
        'is_active',
        'category',
    )
    list_display = (
        'product_name',
        'quantity',
        'price',
        'created_at',
        'sales',
        'is_active',
        'category',
    )
