from django.db import models
from book.models import Book
from account.models import Account

class Order(models.Model):
    books = models.ManyToManyField(Book)
    orderDate = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Account,on_delete = models.CASCADE,blank=True, null=True)