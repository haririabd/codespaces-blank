from django import forms
from django.forms import ClearableFileInput
#from .models import UploadedFile  # If using the model

#class UploadFileForm(forms.ModelForm):
#    class Meta:
#        model = UploadedFile
#        fields = ['file']

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