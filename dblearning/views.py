from django.shortcuts import render
# from .models import Profile

# Create your views here.
def index(request):
    return render(request, 'dblearning/index.html', {})

# def profile_view(request, username):
#     profile = Profile.objects.get(user__username=username)
#     current_user = Profile.objects.get(pk=request.user.id).store.state.name
#     print(current_user)
#     return render(request, 'dblearning/profile.html', {'profile': profile})