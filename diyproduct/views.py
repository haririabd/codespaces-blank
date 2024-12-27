from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'diyproduct/index.html', {})

def purchasing_po(request):
    return render(request, 'diyproduct/neworder.html', {})