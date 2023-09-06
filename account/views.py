from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import ProcessFormView

from account.forms import ForgottenPasswordForm, LoginForm, SignUpForm
from account.models import Client
from account.services.email import send_forgot_message_to_client


class ClientLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = LoginForm


class SignUpView(CreateView):
    template_name = 'account/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    model = Client


class ForgotView(TemplateView):
    template_name = 'account/forgotten-password.html'
    form_class = ForgottenPasswordForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        form = context["form"]
        if form.is_valid():
            form.cleaned_data()
            email = form['email']
            if send_forgot_message_to_client(email=email):
                return redirect('home', context=context)
            else:
                return redirect('home', context=context)




        return redirect('forgot', context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = ForgottenPasswordForm(self.request.POST or None)  # instance= None

        context["form"] = form
        return context

    def send_email_to_client(self, *args, **kwargs):
        # TODO: White services for send email and confirm the token.
        pass

class TokenView(TemplateView):
    pass


def logout_view(request):
    logout(request)
    redirect('home')
