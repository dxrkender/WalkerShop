from django.test import TestCase

from account.forms import ForgottenPasswordForm, LoginForm, SignUpForm


class TestForgottenPasswordForm(TestCase):
    def setUp(self) -> None:
        self.form = ForgottenPasswordForm()

    def test_label(self):
        email_label = self.form.fields['email'].label
        self.assertEqual(email_label, 'Email Address')

    def test_widgets(self):
        email_attrs = self.form.fields['email'].widget.attrs
        excepted_email_attrs = {
            'class': 'form-control',
            'placeholder': 'your@email.com',
            'maxlength': '320',
        }
        self.assertEqual(excepted_email_attrs, email_attrs)

    def test_label_suffix(self):
        label_suffix = self.form.label_suffix
        self.assertEqual(label_suffix, '')


class TestLoginForm(TestCase):

    def setUp(self) -> None:
        self.form = LoginForm()

    def test_labels(self):
        username_label = self.form.fields['username'].label
        password_label = self.form.fields['password'].label
        self.assertEqual(username_label, 'Username')
        self.assertEqual(password_label, 'Password')

    def test_widgets(self):
        username_attrs = self.form.fields['username'].widget.attrs
        password_attrs = self.form.fields['password'].widget.attrs
        excepted_username_attrs = {
            'class': 'form-control',
            'placeholder': 'Your username',
            'label_class': 'form-label',
            'maxlength': 256,
        }

        excepted_password_attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'label_class': 'form-label d-flex justify-content-between align-items-center',
        }

        self.assertEqual(excepted_username_attrs, username_attrs)
        self.assertEqual(excepted_password_attrs, password_attrs)


class TestSignUpForm(TestCase):
    def setUp(self) -> None:
        self.form = SignUpForm()

    def test_labels(self):
        username_label = self.form.fields['username'].label
        email_label = self.form.fields['email'].label
        password_label = self.form.fields['password'].label
        password1_label = self.form.fields['password1'].label
        self.assertEqual(username_label, 'Username')
        self.assertEqual(email_label, 'Email Address')
        self.assertEqual(password_label, 'Password')
        self.assertEqual(password1_label, 'Repeat Password')

    def test_widgets(self):
        username_attrs = self.form.fields['username'].widget.attrs
        email_attrs = self.form.fields['email'].widget.attrs
        password_attrs = self.form.fields['password'].widget.attrs
        password1_attrs = self.form.fields['password1'].widget.attrs
        excepted_username_attrs = {
            'class': 'form-control',
            'placeholder': 'Your username',
            'label_class': 'form-label',
        }

        excepted_email_attrs = {
            'class': 'form-control',
            'placeholder': 'name@email.com',
            'label_class': 'form-label',
            'maxlength': '320',
        }

        excepted_password_attrs = {
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'label_class': 'form-label d-flex justify-content-between align-items-center',
        }

        excepted_password1_attrs = {
            'class': 'form-control',
            'placeholder': 'Repeat your password',
            'label_class': 'form-label d-flex justify-content-between align-items-center',
        }

        self.assertEqual(excepted_username_attrs, username_attrs)
        self.assertEqual(excepted_email_attrs, email_attrs)
        self.assertEqual(excepted_password_attrs, password_attrs)
        self.assertEqual(excepted_password1_attrs, password1_attrs)


    def test_clean_password(self):
        form = SignUpForm(
            data={
                "username": "testusername",
                "email": "test@username.com",
                "password": "Testpassword1",
                "password1": "Testpassword2",
            })
        form.is_valid()
        form.clean()

        self.assertTrue(form.errors)

        form = SignUpForm(
            data={
                "username": "testusername",
                "email": "test@username.com",
                "password": "Testpassword1",
                "password1": "Testpassword1",
            })

        self.assertFalse(form.errors)