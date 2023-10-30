"""
URL configuration for WalkerShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/

    Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import (  # isort:skip
    ClientLoginView,
    ResetPasswordView,
    SignUpView,
)

urlpatterns = [
    path('', ClientLoginView.as_view(), name='account_index'),
    path('login/', ClientLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('reset/', ResetPasswordView.as_view(), name='reset'),
    path('reset/<str:token>', ResetPasswordView.as_view(), name='token'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]
