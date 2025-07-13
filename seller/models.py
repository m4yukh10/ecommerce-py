from django.db import models

# Create your models here.
class Seller(models.Model):
    name = models.CharField(max_length=150)
    pickupAddress = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    


class Products(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    type = models.CharField(max_length=100)
    quantity = models.IntegerField()

        