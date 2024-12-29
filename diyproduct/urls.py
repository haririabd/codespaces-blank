from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('new-order/upload/', views.upload_handheld, name='upload_handheld'),
]