"""Add endpoints for url `/` in path."""

from django.views.generic import TemplateView


class IndexView(TemplateView):
    """It's a view for index page."""

    template_name = 'shop/index.html'


class CategoryView(TemplateView):
    """It's a view for category page."""

    template_name = 'shop/category.html'


class ProductView(TemplateView):
    """It's a view for product page."""

    template_name = 'shop/product.html'
