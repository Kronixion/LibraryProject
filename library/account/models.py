from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Address(models.Model):
    street = models.CharField(max_length=50)
    streetNo = models.IntegerField()
    apartmentNo = models.IntegerField()
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.street + " " + str(self.streetNo) + " " + str(self.apartmentNo)

class ShoppingCart(models.Model):
    books = models.ManyToManyField(Book,blank=True, null=True)

    def __str__(self):
        return str(self.id)
    
    def sumOfBooks(self):
        sum=0
        for book in self.books.all():
            sum+=int(book.price)
        return sum

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNo = models.CharField(max_length=10)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    shoppingCart = models.OneToOneField(ShoppingCart,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username