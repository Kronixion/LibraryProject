from django.db import models
from django.contrib.auth.models import User
from purchases.models import ShoppingCart, Order

class Address(models.Model):
    street = models.CharField(max_length=50)
    streetNo = models.IntegerField()
    apartmentNo = models.IntegerField()
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNo = models.CharField(max_length=10)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)