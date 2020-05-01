from django.shortcuts import render
from account.models import Account
from .models import RentRequest
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@login_required
@csrf_exempt
def rent(request):
    account = Account.objects.get(id=request.user.id)
    book = Book.objects.get(id=request.POST['bookId'])
    print(book)
    if request.method == 'POST':
        rentRequest = RentRequest(user = account,book=book)
        rentRequest.save()
        return HttpResponse('You have rented the book ' + book.title + ' !')
    else:
        rentedRequests = RentRequests.objects.filter(user = account)
        return render(request,'rentPage.html',{'rentedRequests':rentedRequests})