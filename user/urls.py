# user/urls.py
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register_buyer, name="register_buyer"),
    path('login', views.login_buyer, name="login_buyer"),
    path('buy', views.buy_product, name='buy'),
    
]
