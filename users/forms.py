from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from users.models import User
from django.core import validators


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя'
        }),
        validators=[validators.RegexValidator(regex='^(?=[a-zA-Z0-9._]{3,20}$)(?!.*[_.]{2})[^_.].*[^_.]$')],
        error_messages={
            'invalid': 'Login должен быть длинее 3 символов, И может соделжать латинские буквы, знаки "_" и "." '}
    )
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите адрес эл. почты'
        }))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя'
        }),
        validators=[validators.RegexValidator(regex='^.{3,}$')],
        error_messages={'invalid': 'Имя не может быть короче 3 символов'})
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите фамилию'
        }),
        validators=[validators.RegexValidator(regex='^.{3,}$')],
        error_messages={'invalid': 'Фамилия не может быть короче 3 символов'}
    )
    # image = forms.ImageField()

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control py-4',
            'placeholder': 'Подтвердите пароль'
        }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
