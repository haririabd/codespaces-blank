from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select
# from django.forms import ClearableFileInput
#from .models import UploadedFile  # If using the model

#class UploadFileForm(forms.ModelForm):
#    class Meta:
#        model = UploadedFile
#        fields = ['file']

class CreateStaffForm(UserCreationForm):
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
        fields = ['username', 'email', 'first_name', 'last_name', 'groups' ]
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Username",
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': "Email",
            }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': "First Name",
            }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Last Name",
            }),
            'groups': Select(attrs={
                'class': "form-control",
                'placeholder': "Permission",
            })
        }

# If not using the model
class UploadHandheld(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        label='Select a .txt only file',
        validators=[
            lambda file: file.name.endswith('.txt') or 
            forms.ValidationError("Only .txt files are allowed.")
        ]
    )

class manualAddItem(forms.Form):
    sku = forms.IntegerField(widget = forms.TextInput)
    quantity = forms.IntegerField(widget = forms.TextInput)