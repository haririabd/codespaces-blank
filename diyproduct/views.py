from django.shortcuts import render
from .forms import UploadHandheld
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'diyproduct/index.html', {})

def new_order(request):
    return render(request, 'diyproduct/new_order.html', {})

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
            po_items = []

            # Process the file content (e.g., parse data, extract information) 
            for line in file_content.splitlines():
                if not line.strip(): # Check if the line is empty
                    continue # Skip empty lines

                try:
                    sku,quantity = line.strip().split(',', 1)
                    po_items.append({'sku': int(sku), 'quantity': int(float(quantity))})
                except ValueError:
                    # Handle invalid lines (e.g., incorrect format)
                    print(f"Invalid line: {line}")
                    continue

            return render(request, 'diyproduct/upload_handheld.html', {'po_items': po_items})
        
    else:
        form = UploadHandheld()
    return render(request, 'diyproduct/upload_handheld.html', {'form': form})