from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from admins.forms import CategoryNewAdminForm, ProductAdminForm

from products.models import ProductCategory, Product

from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


# READ
@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {'title': 'GeekShop - Админ | Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {'title': 'GeekShop - Админ | Регистрация', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Данные успешно сохранены')
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'GeekShop - Admin | Обновление пользователя',
               'form': form,
               'selected_user': selected_user,
               }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {'title': 'GeekShop - Админ | Категории', 'categories': ProductCategory.objects.all()}
    return render(request, 'admins/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoryNewAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoryNewAdminForm()
    context = {'title': 'GeekShop - Админ | Создание категории', 'form': form}
    return render(request, 'admins/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_update(request, id):
    selected_category = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryNewAdminForm(data=request.POST, instance=selected_category)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Данные успешно сохранены')
            return HttpResponseRedirect(reverse('admins:admin_categories'))
    else:
        form = CategoryNewAdminForm(instance=selected_category)
    context = {'title': 'GeekShop - Admin | Обновление категории',
               'form': form,
               'selected_category': selected_category,
               }
    return render(request, 'admins/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_delete(request, id):
    category = ProductCategory.objects.get(id=id)
    category.is_active = False
    category.save()
    return HttpResponseRedirect(reverse('admins:admin_categories'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {'title': 'GeekShop - Админ | Товары', 'products': Product.objects.all()}
    return render(request, 'admins/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_create(request):
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.is_active = True
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_products'))
        else:
            print(form.errors)
    else:
        form = ProductAdminForm()
    context = {'title': 'GeekShop - Админ | Новый товар', 'form': form}
    return render(request, 'admins/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_update(request, id):
    selected_product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST, files=request.FILES, instance=selected_product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно сохранены')
            return HttpResponseRedirect(reverse('admins:admin_products'))
        else:
            print(form.errors)
    else:
        form = ProductAdminForm(instance=selected_product)
    context = {'title': 'GeekShop - Admin | Обновление товара',
               'form': form,
               'selected_product': selected_product,
               }
    return render(request, 'admins/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reverse('admins:admin_products'))
