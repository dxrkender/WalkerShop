"""The module contains django from for account application."""
from typing import Any, Dict

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import ModelFormMetaclass

from account.models import Client


class AccountFormMixin(object):
    """Mixin class for authentication and authorization."""

    @classmethod
    def get_field_attrs(
        cls,
        placeholder: str,
        field_class: str = 'form-control',
        label_class: str = 'form-label',
    ) -> Dict[str, str]:
        """Create attrs for authentication and authorization.

        Create pre-prepared dictionary with incoming function parameters.

        Args:
            placeholder (str): Attribute for input tag on form
                which sets the default value.
            field_class (str): Attribute for input tag on form
                which sets the class value.
            label_class (str): Attribute for input tag on form
                which sets the label class value.

        Returns:
            default_atts (Dict[str, str]): A dict containing attributes
              and their values for the field.
        """
        return {
            'class': field_class,
            'label_class': label_class,
            'placeholder': placeholder,
        }


class ForgottenPasswordForm(AccountFormMixin, PasswordResetForm):
    """The form for recover user's password from email.

    The form is used in a situation where
    the client has forgotten his password.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        """Added empty text for from label.

        Default text is `:` and it isn't prettify.

        Args:
            args (Any): Passing args to the parent's constructor.
            kwargs (Any): Passing kwargs to the parent's constructor.

        Keyword Args:
            label_suffix (str): String before label text.
        """
        kwargs['label_suffix'] = ''
        super().__init__(*args, **kwargs)

    email_max_length = 254

    email = forms.EmailField(
        label='Email Address',
        max_length=email_max_length,
        widget=forms.EmailInput(
            attrs=AccountFormMixin.get_field_attrs(
                placeholder='your@email.com',
            ),
        ),
    )


class LoginForm(AccountFormMixin, AuthenticationForm):
    """The form authenticated user in services."""

    class Meta(ModelFormMetaclass):
        """Metaclass for classes for media forms definitions."""

        model = User
        fields = (
            'username',
            'password',
        )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs=AccountFormMixin.get_field_attrs(
                placeholder='Your username',
            ),
        ),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs=AccountFormMixin.get_field_attrs(
                placeholder='Enter your password',
                label_class=(
                    'form-label d-flex justify-content-between ' +
                    'align-items-center'
                ),
            ),
        ),
    )


class SignUpForm(AccountFormMixin, forms.ModelForm):
    """The form register user in services."""

    class Meta(ModelFormMetaclass):
        """Metaclass for classes for media definitions."""

        model = Client
        fields = (
            'username',
            'email',
            'password',
        )

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs=AccountFormMixin.get_field_attrs(
                placeholder='Your username',
            ),
        ),
    )

    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(
            attrs=AccountFormMixin.get_field_attrs(
                placeholder='your@email.com',
            ),
        ),
    )

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs=AccountFormMixin.get_field_attrs(
                placeholder='Enter your password',
                label_class=(
                    'form-label d-flex justify-content-between ' +
                    'align-items-center'
                ),
            ),
        ),
    )

    password1 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput(
            attrs=AccountFormMixin.get_field_attrs(
                placeholder='Repeat your password',
                label_class=(
                    'form-label d-flex justify-content-between ' +
                    'align-items-center'
                ),
            ),
        ),
    )

    def clean_password1(self):
        """Validate repeat password field.

        The validator checks the equality of two fields `password` and
        'password1'. If these fields are equal each other method doesn't raise
        ValidationError and return value of the 'password1' field.

        Returns:
            Returns cleaned value of the password1 field

        Raises:
            ValidationError: Password values don't match.
        """
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise ValidationError('Password mismatch.')
        return password1

    def save(self, commit: bool = True) -> Client:
        """Add saving user password.

        Args:
            commit (bool): Writing to database during save.

        Returns:
            New Client instance.
        """
        client = super().save(commit=False)
        client.set_password(self.cleaned_data['password'])
        if commit:
            client.save()
        return client
