from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    username = forms.CharField(
        label='Login',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your login'})
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        help_text='The password should not be small and simple',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
    )
    password2 = forms.CharField(
        label='Submit password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Reenter your password'})
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
