from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'seller'

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register_seller', views.register_seller, name="registeruser"),
    path('products', views.products, name="products"),
    
    
    
    
    
]