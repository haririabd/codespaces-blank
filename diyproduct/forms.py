from django import forms
#from .models import UploadedFile  # If using the model

#class UploadFileForm(forms.ModelForm):
#    class Meta:
#        model = UploadedFile
#        fields = ['file']

# If not using the model
class UploadHandheld(forms.Form):
    file = forms.FileField(
        label='Select a .txt file',
        help_text='Only .txt files are allowed.',
        validators=[
            lambda file: file.name.endswith('.txt') or 
            forms.ValidationError("Only .txt files are allowed.")
        ]
    )