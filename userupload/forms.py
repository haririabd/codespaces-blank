from django import forms

# https://studygyaan.com/django/import-data-from-csv-sheets-into-databases-using-django
class CSVimportForm(forms.Form):
    csv_file = forms.FileField()