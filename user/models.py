from django.db import models
from seller.models import Products

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=1000)
    age = models.IntegerField()
    address = models.CharField(max_length=10000)
    
    
class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    created_at = models.DateTimeField(auto_now_add=True)
        