from django import forms
from apps.user.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SingupForm(UserCreationForm):
    """Создание формы для регистрации"""

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }
