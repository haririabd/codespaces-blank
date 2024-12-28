from django.shortcuts import render
from .forms import UploadHandheld
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'diyproduct/index.html', {})

def upload_handheld(request):
    if request.method == 'POST':
        form = UploadHandheld(request.POST, request.FILES)
        if form.is_valid():
            # Option 1: Save the file (Recommended for long-term storage)
            # uploaded_file = form.save() 
            # message = f"File '{uploaded_file.file.name}' uploaded successfully."

            # Option 2: Process the file directly (No need to save)
            file = request.FILES['file'] 
            # Read the file content (example with utf-8 encoding)
            file_content = file.read().decode('utf-8') 
            # Process the file content (e.g., parse data, extract information) 
            # ...

            return HttpResponse("File uploaded successfully.")
    else:
        form = UploadHandheld()
    return render(request, 'diyproduct/neworder.html', {'form': form})