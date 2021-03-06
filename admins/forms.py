from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from django import forms


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