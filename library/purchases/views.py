from django.shortcuts import render,redirect
from account.models import Account
from .models import Order
from django.http import HttpResponse

def orders(request):
    account = Account.objects.get(id = request.user.id)
    order = account.shoppingCart.books.all()
    orders = Order.objects.filter(user=account)
    if request.method == "POST" and len(order)!=0:
        o = Order(user=account,totalSum=account.shoppingCart.sumOfBooks())
        o.save()
        for book in order:
            o.books.add(book)
        account.shoppingCart.books.clear()
        return render(request,'orders.html',{'orders':orders})
    else:
        return render(request,'orders.html',{'orders':orders})

def detailedOrder(request,id):
    account = Account.objects.get(id=request.user.id)
    order = Order.objects.get(id=id)
    if order.user == account:
        return render(request,'detailedOrder.html',{'orders':order.books.all(),'totalNumberOfItems':len(order.books.all()),'totalSum':order.totalSum,'id':id})
    return render(request,'detailedOrder.html',{'message':'Order not found...'})