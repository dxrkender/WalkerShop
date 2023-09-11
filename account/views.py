from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


from account.forms import ForgottenPasswordForm, LoginForm, SignUpForm
from account.models import Client


class ClientLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm


class SignUpView(CreateView):
    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    model = Client


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')
    subject_template_name = 'account/password_reset_subject.txt'
    form_class = ForgottenPasswordForm


def logout_view(request):
    logout(request)
    redirect('home')
