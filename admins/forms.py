from users.forms import UserRegisterForm, UserProfileForm
from products.models import ProductCategory, Product
from users.models import User
from django import forms
from django.forms import ModelForm


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'custom-file-input'
        }),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'readonly': False
        }))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control py-4',
            'readonly': False
        }))


class CategoryNewAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите название категории'
        }))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите краткое описание категории'
        }), required=False)
    is_active = forms.BooleanField(initial=True)

    class Meta:
        model = ProductCategory
        fields = ('name', 'description', 'is_active')


class ProductAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите краткое описание категории'
        }),
        max_length=256)
    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'custom-file-input'
        }),
        required=False)
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите краткое описание категории'
        }),
        max_length=64, required=False)
    price = forms.DecimalField(min_value=0, max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(min_value=0)
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(), empty_label=None)
    is_active = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category', 'is_active')
