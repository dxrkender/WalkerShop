"""Module for customizing admin interface for this application."""
from typing import Dict, Tuple

from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput

from cart.models import (
    AudienceCategory,
    Product,
    ProductCategory,
    ProductSubcategory,
)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """Customizing admin interface for `ProductCategory` model.

    Attributes:
        fields (Tuple[str]): Fields of model instance which
            will be able to add or change in forms.

        list_display (Tuple[str]):
            Fields which will be displayed admin interface.
    """

    fields: Tuple[str] = ('category_name', 'category_description')
    list_display: Tuple[str] = ('category_name', 'category_description')


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
    list_display: Tuple[str] = (
        'product_name',
        'quantity',
        'price',
        'created_at',
        'sales',
        'is_active',
        'category',
    )


@admin.register(AudienceCategory)
class AudienceCategoryAdmin(admin.ModelAdmin):
    """Customizing admin interface for `ClientAudienceCategoryAdmin` model.

    Attributes:
        fields (Tuple[str]): Fields of model instance which
            will be able to add or change in forms.

        list_display (Tuple[str]):
            Fields which will be displayed admin interface.

        formfield_overrides (Dict):
            This provides a quick-and-dirty way to override some of
            the Field options for use in the admin.
    """

    _text_area_rows = 5
    _text_area_cols = 100
    _text_area_length = 97

    fields: Tuple[str] = (
        'audience_name',
        'audience_description',
        'categories',
    )
    list_display: Tuple[str] = ('audience_name', 'audience_description')

    formfield_overrides: Dict = {
        models.CharField: {
            'widget': TextInput(attrs={
                'size': _text_area_length,
            }),
        },
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': _text_area_rows,
                'cols': _text_area_cols,
            }),
        },
    }


@admin.register(ProductSubcategory)
class ProductSubcategoryAdmin(admin.ModelAdmin):
    """Customizing admin interface for `ProductCategory` model.

    Attributes:
        fields (Tuple[str]): Fields of model instance which
            will be able to add or change in forms.

        list_display (Tuple[str]):
            Fields which will be displayed admin interface.
    """

    fields: Tuple[str] = ('subcategory_name',)
    list_display: Tuple[str] = ('subcategory_name',)
