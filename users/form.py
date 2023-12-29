from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from datetime import date

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Remove help text for the password1 field
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''
    email = forms.EmailField()
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        min_age = 10
        if dob:
            age = (date.today() - dob).days // 365
            if age < min_age:
                raise ValidationError(f'You must be at least {min_age} years old to register.')
        return dob

    class Meta:
        model = CustomUser
        fields = ["username", "email", "date_of_birth", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''

    email = forms.EmailField()
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        min_age = 10
        if dob:
            age = (date.today() - dob).days // 365
            if age < min_age:
                raise ValidationError(f'You must be at least {min_age} years old to register.')
        return dob
    class Meta:
        model = CustomUser
        fields = ["username", "email", "date_of_birth"]