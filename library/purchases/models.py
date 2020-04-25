from django.db import models
from book.models import Book

class ShoppingCart(models.Model):
    books = models.ManyToManyField(Book)
    totalSum = models.IntegerField(default=0)

class Order(models.Model):
    books = models.ManyToManyField(Book)
    orderDate = models.DateTimeField(auto_now=True)
    totalSum = models.IntegerField()