from django.shortcuts import render
from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'dblearning/index.html', {})

def profile_view(request, username):
    profile = Profile.objects.get(user__username=username)
    return render(request, 'dblearning/profile.html', {'profile': profile})