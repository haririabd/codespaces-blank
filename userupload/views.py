from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CSVimportForm
from dblearning.models import Store
import csv

# https://studygyaan.com/django/import-data-from-csv-sheets-into-databases-using-django
def import_csv(request):
    form = CSVimportForm()

    if request.method == 'POST':
        form = CSVimportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)

            # for row in csv_reader:
            #     Store.objects.create(
            #         title=row['title'],
            #         author=row['author'],
            #         publication_year=row['publication_year'],
            #         isbn=row['isbn']
            #     )

            return redirect('import_store')  # Redirect to a success page
    else:
        form = CSVimportForm()

    return render(request, 'userupload/upload.html', {'form': form})
