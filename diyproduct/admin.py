from django.contrib import admin
from .models import Category, Store, PurchaseOrder

# Register your models here.
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(PurchaseOrder)