from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('profile/<str:username>/', views.profile_view, name='profile_view'),
]