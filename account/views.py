"""Add endpoints for url `/account` in path."""
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import ForgottenPasswordForm, LoginForm, SignUpForm
from account.models import Client


class ClientLoginView(LoginView):
    """View for authentication and authorization.

    Display the template `account/login.html` and
    add the form `LoginForm` in template.
    """

    template_name = 'account/login.html'
    form_class = LoginForm


class SignUpView(CreateView):
    """View for create new client in service.

    Display the template `account/signup.html` and add the form 'SignUpForm'.
    The success url is the path to which client will be redirected
    if it's authenticated.
    Client automatically will be created such as Client instance
    from account.models.
    """

    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    model = Client


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """View for password reset by the client.

    Display templates:
    `account/password_reset.html`, `account/password_reset_email.html`.
    Add the form 'ForgottenPasswordForm'.
    Email template name need to display template in email letter
    with subject template name.
    The success url is the path to which client will be redirected
    if it's authenticated.
    """

    success_text = """
        We've emailed you instructions for setting your password, if an 
        account exists with the email you entered. You should receive them 
        shortly. If you don't receive an email, please make sure you've entered 
        the address you registered with, and check your spam folder.
    """
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    success_message = (success_text)
    success_url = reverse_lazy('login')
    subject_template_name = 'account/password_reset_subject.txt'
    form_class = ForgottenPasswordForm


def logout_view(request: WSGIRequest):
    """Logout a client from the service.

    Args:
        request (WSGIRequest): object for http request.

    Returns (None):
        The function does not return anything,
        it only calls the `logout` function.
    """
    logout(request)
    redirect('home')
