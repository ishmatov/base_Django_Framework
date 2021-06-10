from django.shortcuts import render
from products.models import Product, ProductCategory
import json
import os


MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт',
        'username': 'Ишматов Руслан',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Каталог товаров GeekShop',
        'username': 'Ишматов Руслан',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
