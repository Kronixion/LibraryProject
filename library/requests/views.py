from django.shortcuts import render
from account.models import Account
from .models import RentRequest
from book.models import Book
from django.contrib.auth.decorators import login_required

@login_required
def rent(request):
    account = Account.objects.get(request.id)
    if request.method == 'POST':
        rentRequest = RentRequest(user = account, book = Book.objects.get(request.POST['bookId']))
        rentRequest.save()
    else:
        rentedRequests = RentRequests.objects.filter(user = account)
        return render(request,'rentPage.html',{'rentedRequests':rentedRequests})