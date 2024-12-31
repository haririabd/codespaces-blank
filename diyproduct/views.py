from django.shortcuts import render
from .forms import UploadHandheld, manualAddItem
import datetime
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'diyproduct/index.html', {})

def orders(request):
    return render(request, 'diyproduct/orders.html', {})

def create_order(request):
    if request.user.is_authenticated:
        prefix = User.objects.get(pk=request.user.id).profile.store.brand
        num1 = int(datetime.datetime.now().strftime("%d%m%y%H%M%S"))
        ordernum = f'{prefix} - {str(num1)}'
        context = {
            'ordernum': ordernum,
        }
        return render (request, 'diyproduct/new_order.html', context)
    else:
        context = {}
        return render (request, 'diyproduct/new_order.html', context)

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
            error_items = []

            # Process the file content (e.g., parse data, extract information) 
            for line in file_content.splitlines():
                if not line.strip(): # Check if the line is empty
                    continue # Skip empty lines

                try:
                    sku,quantity = line.strip().split(',', 1)
                    po_items.append({'sku': int(sku), 'quantity': int(float(quantity))})
                except ValueError:
                    # Handle invalid lines (e.g., incorrect format)
                    error_items.append({'line': line})
                    continue
            context = {
                'po_items': po_items,
                'error_items': error_items,
                'total_item': len(po_items),
                'total_error': len(error_items)
            }
            return render(request, 'diyproduct/display_handheld.html', context)
        
    else:
        form = UploadHandheld()
    return render(request, 'diyproduct/upload_handheld.html', {'form': form})

# def manualAddItem(request):
#     if request.method == 'POST':
#         form = manualAddItem(request.POST)
#         sku = 0
#         quantity = 0
#         if form.is_valid():
#             print(sku, quantity)