from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('create-order/', views.create_order, name='create_order'),
    path('new-order/upload/', views.upload_handheld, name='upload_handheld'),
    path('staff/', views.staffPage, name='staffpage'),
    path('profile/', views.userProfile, name='profilePage'),
    path('create-staff', views.create_staff, name='create_staff'),
]