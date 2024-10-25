from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.user.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'alias', 'avatar')

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
        # Django form trabaja con widgets
        # Los widgets son los elementos que se renderizan en el HTML
        # Pueden recibir atributos como clases, id, placeholder, etc
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )