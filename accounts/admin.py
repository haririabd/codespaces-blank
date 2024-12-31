from django.contrib import admin

# Register your models here.
from .models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User) # Necessary

class UserProfileInline(admin.TabularInline):
    model = Profile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)