from django.shortcuts import render
from account.models import Account
from .models import Order

def orders(request):
    account = Account.objects.get(id = request.user.id)
    order = account.shoppingCart.books.all()
    if request.method == "POST":
        o = Order(user=account)
        o.save()
        for book in order:
            o.books.add(book)
        account.shoppingCart.books.clear()
        return redirect('/orders/')
    else:
        orders = Order.objects.filter(user=account)
        return render(request,'orders.html',{'orders':orders})

def detailedOrder(request):
    pass