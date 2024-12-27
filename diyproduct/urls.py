from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('new-order/', views.purchasing_po, name='purchasing_po'),
]