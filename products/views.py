from django.shortcuts import render
import json


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт',
        'username': 'Ишматов Руслан',
    }
    return render(request, 'products/index.html', context)


def products(request):
    # with open(r"fixtures\products.json", "r") as f_products:
    #     items = json.load(f_products)

    context = {
        'title': 'Каталог товаров GeekShop',
        'username': 'Ишматов Руслан',
         # 'products': items['products']
         'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6_090, 'img': 'Adidas-hoodie.png', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': 23_725, 'img': 'Blue-jacket-The-North-Face.png', 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3_390, 'img': 'Brown-sports-oversized-top-ASOS-DESIGN.png', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2_340, 'img': 'Black-Nike-Heritage-backpack.png', 'description': 'Плотная ткань. Легкий материал.'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13_590, 'img': 'Black-Dr-Martens-shoes.png', 'description': 'Гладкий кожаный верх. Натуральный материал.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2_890, 'img': 'Dark-blue-wide-leg-ASOs-DESIGN-trousers.png', 'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'}
        ]
    }
    return render(request, 'products/products.html', context)

# def test_context(request):
#     return render(request, 'products/test-context.html')
