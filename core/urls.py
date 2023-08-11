from django.urls import path

from core.views import IndexView, ProductView, CategoryView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('product/', ProductView.as_view(), name='product'),
    path('category/', CategoryView.as_view(), name='category'),
]
