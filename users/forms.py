import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)
from django.utils.timezone import now

from users.models import EmailVerification, User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Enter your username",
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Enter your password",
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите имя пользователя",
    }))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль",
    }))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Повторите пароль",
    }))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите имя",
    }))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите фамилию",
    }))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите email",
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
        'readonly': True,
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4',
        'readonly': True,
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4',
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'image', 'first_name', 'last_name', 'email')
