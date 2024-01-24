"""Add endpoints for url `/cart` in path."""

from django.views.generic import TemplateView


class CartView(TemplateView):
    """View for user's cart."""

    template_name = 'cart/cart.html'


class CheckoutCartView(TemplateView):
    """View for checkout user's cart."""

    template_name = 'cart/checkout.html'


class ShippingCartView(TemplateView):
    """View for checkout shipping user's cart."""

    template_name = 'cart/shipping.html'


class PaymentCartView(TemplateView):
    """View for checkout payment user's cart."""

    template_name = 'cart/payment.html'


class OrdersCartView(TemplateView):
    """View for user's orders and their stage."""

    template_name = 'cart/orders.html'
