from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
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


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your username',
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


class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your username',
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

    password1 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat your password',
                'label_class': 'form-label d-flex justify-content-between align-items-center',
            }
        ),
    )

    class Meta:
        model = Client
        fields = ('username', 'email', 'password')

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise ValidationError('Password mismatch.')
        else:
            return password1

    def save(self, commit=True):
        client = super().save(commit=False)
        client.set_password(self.cleaned_data['password'])
        if commit:
            client.save()
        return client
