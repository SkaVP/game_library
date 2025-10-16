from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Game
from django import forms

# форма регистрации

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# добавление игры

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'description', 'genre', 'release_date']

# редактирование профиля

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']