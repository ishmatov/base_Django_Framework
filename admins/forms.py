from users.forms import UserRegisterForm
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
