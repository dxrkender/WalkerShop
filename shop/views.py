from django.shortcuts import render
from django.views.generic import TemplateView


<<<<<<< HEAD
class IndexShopView(TemplateView):
    template_name = 'shop/index.html'

class CategoryView(TemplateView):
    template_name = 'shop/category.html'


class ProductView(TemplateView):
    template_name = 'shop/product.html'
=======
class HomeView(TemplateView):
    pass
>>>>>>> develop
