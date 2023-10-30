"""Add endpoints for url `/cart` in path."""

from django.views.generic import TemplateView


class CartView(TemplateView):
    """View for user's cart."""

    template_name = ''
