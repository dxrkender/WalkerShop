from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from account.models import Client


class ForgottenPasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)

    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com'
            }
        )
    )


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_classes = {
            'email_label': 'login-email',
            'password_label': 'form-label d-flex justify-content-between align-items-center',
        }

    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'name@email.com',
                'label_class': 'form-label',
            }
        ),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
                'label_class': 'form-label d-flex justify-content-between align-items-center',
            }
        ),
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User123',
                'label_class': 'form-label',
            }
        ),
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'name@email.com',
                'label_class': 'form-label',
            }
        ),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password',
                'label_class': 'form-label d-flex justify-content-between align-items-center',
            }
        ),
    )

    repeat_password = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat your password',
                'label_class': 'form-label d-flex justify-content-between align-items-center',
            }
        ),
    )

    def clean_password(self):
        password = self.cleaned_data['password']
        repeat_password = self.cleaned_data['repeat_password']
        if password != repeat_password:
            ValidationError('Password mismatch.')
        else:
            return True
