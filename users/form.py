from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth=forms.DateField()

    class Meta:
        model = User
        fields = ["username", "email", "date_of_birth", "password1", "password2"]
