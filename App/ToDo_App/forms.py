from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class RegisterForm(UserCreationForm):
    # Removing is_admin and is_user as they can be set programmatically
    email = forms.EmailField(  # EmailField for better validation
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')  # Removed is_admin and is_user
