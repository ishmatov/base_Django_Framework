from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from django.urls import reverse


def index(request):
    return render(request, 'admins/admin.html')


# READ
def admin_users(request):
    context = {'title': 'GeekShop - Админ | Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)


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


def admin_users_delete(request, id):
    pass
