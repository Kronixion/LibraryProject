from django.contrib import admin
from .models import Account, Address, ShoppingCart

admin.site.register(Account)
admin.site.register(Address)
admin.site.register(ShoppingCart)