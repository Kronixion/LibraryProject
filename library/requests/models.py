from django.db import models
from account.models import Account
from book.models import Book
from django.utils.translation import gettext_lazy as _

class RentRequest(models.Model):
    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    user = models.ForeignKey(Account, on_delete= models.CASCADE)

class ExchangeRequest(models.Model):
    book = models.ForeignKey(Book, on_delete= models.CASCADE)
    user = models.ForeignKey(Account, on_delete= models.CASCADE)
    bookTitle = models.CharField(max_length=50)
    bookAuthor = models.CharField(max_length=50)

    class State(models.TextChoices):
        DAMAGED = 'DM', _('DAMAGED')
        USED = 'US', _('USED')
        NEW = 'NE', _('NEW')

    bookState = models.CharField(max_length=2,choices=State.choices)
    bookImage = models.ImageField(upload_to='exchangeBooks/')