from django.contrib import admin
from .models import ProductCategory, Store, PurchaseOrder, User, State, Brand

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(PurchaseOrder)
admin.site.register(State)
admin.site.register(Brand)

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "store")

admin.site.register(User, UserAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ("store_name", "brand", "store_code", "state")

admin.site.register(Store, StoreAdmin)