from django.shortcuts import render
from django.views.generic import TemplateView


class CategoryView(TemplateView):
    template_name = 'core/category.html'


class IndexView(TemplateView):
    template_name = 'core/index.html'


class ProductView(TemplateView):
    template_name = 'core/product.html'
