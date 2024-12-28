from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('new-order/', views.upload_handheld, name='new_order'),
]