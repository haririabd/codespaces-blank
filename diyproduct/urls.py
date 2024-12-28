from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('new-order/', views.new_order, name='new_order'),
    path('new-order/upload/', views.upload_handheld, name='upload_handheld'),
]