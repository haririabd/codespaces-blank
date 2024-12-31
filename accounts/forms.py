# user form below from https://www.youtube.com/watch?v=tUqUdu0Sjyc
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, EmailInput

# forms widget for styling.
# reference from https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Password'}),
    )
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Username",
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': "Email",
            })
        }