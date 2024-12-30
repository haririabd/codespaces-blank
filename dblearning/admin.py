from django.contrib import admin
from .models import State, Category, Store, Brand
# Register your models here.

admin.site.register(State)
admin.site.register(Category)
admin.site.register(Brand)


class StoreAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "state")

admin.site.register(Store, StoreAdmin)