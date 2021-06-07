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
    file_path = os.path.join(MODULE_DIR, 'fixtures/products.json')
    with open(file_path, "r") as f_products:
        items = json.load(f_products)
    context = {
        'title': 'Каталог товаров GeekShop',
        'username': 'Ишматов Руслан',
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)
