from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop.views import IndexShopView, CategoryView, ProductView

urlpatterns = [
    path('', IndexShopView.as_view(), name='index'),
    # path('category/<slug:category_slug>', CategoryView.as_view(), name='category'),
    # path('product/<slug:product_slug>', ProductView.as_view(), name='product'),
    path('category', CategoryView.as_view(), name='category'),
    path('product', ProductView.as_view(), name='product'),
]
