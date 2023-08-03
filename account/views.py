from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from account.forms import ForgottenPasswordForm, LoginForm, SignUpForm


class LoginView(TemplateView):
    template_name = 'login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            redirect('home')

        return redirect('home', context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = LoginForm(self.request.POST or None)  # instance= None

        context["form"] = form
        return context


class SignUpView(TemplateView):
    template_name = 'signup.html'
    form_class = SignUpForm

    def post(self, *args, **kwargs):
        print(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = SignUpForm(self.request.POST or None)  # instance= None

        context["form"] = form
        return context


class ForgotView(TemplateView):
    template_name = 'forgotten-password.html'
    form_class = ForgottenPasswordForm

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            redirect('home')

        return redirect('forgot', context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = ForgottenPasswordForm(self.request.POST or None)  # instance= None

        context["form"] = form
        return context


def logout_view(request):
    logout(request)
    redirect('home')
