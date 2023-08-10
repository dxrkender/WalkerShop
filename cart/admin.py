from django.contrib import admin

from cart.models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('category_name',)
    list_display = ('category_name',)


@admin.register(Product)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('product_name', 'quantity', 'price', 'created_at',
              'sales', 'is_active', 'category')
    list_display = ('product_name', 'quantity', 'price', 'created_at',
                    'sales', 'is_active', 'category')
