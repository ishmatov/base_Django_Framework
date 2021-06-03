from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


def test_context(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт!',
        'username': 'Ишматов Руслан',
        'products': [
            # {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6_090},
            # {'name': 'Синяя куртка The North Face', 'price': 23_725},
            # {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3_390},
            # {'name': 'Черный рюкзак Nike Heritage', 'price': 2_340},
            # {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13_590},
            # {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2_890}
        ]
    }
    return render(request, 'products/test-context.html', context)
