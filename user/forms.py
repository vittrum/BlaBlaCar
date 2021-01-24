from django import forms

from user.models import User


class LoginForm(forms.Form):
    phone = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    model = User
    fields = [
        'phone',
        'password',
        'name',
        'lastname'
    ]

