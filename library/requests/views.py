from django.shortcuts import render,redirect
from account.models import Account
from .models import RentRequest, ExchangeRequest
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import RequestExchangeForm
from django.contrib.admin.views.decorators import staff_member_required

@login_required
@csrf_exempt
def rent(request):
    account = Account.objects.get(id=request.user.id)
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['bookId'])
        rentRequest = RentRequest(user = account,book=book)
        rentRequest.save()
        return HttpResponse('You have rented the book ' + book.title + ' !')
    else:
        rentedRequests = RentRequest.objects.filter(user = account)
        return render(request,'rentPage.html',{'rentedRequests':rentedRequests})

@login_required
def exchangeRequestForm(request,id):
    if request.method == 'POST':
        form = RequestExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            exchangeRequest = form.save(commit=False)
            exchangeRequest.book = Book.objects.get(id=id)
            exchangeRequest.user=Account.objects.get(id=request.user.id)
            exchangeRequest.save()
        return redirect('/searchBooks/')
    else:
        form  = RequestExchangeForm()
        book = Book.objects.get(id=id)
        return render(request, 'exchangeForm.html',{'form':form,'book':book})

@login_required
@staff_member_required
def staffDashboard(request):
    rentRequests = RentRequest.objects.all()
    exchangeRequests = ExchangeRequest.objects.all()
    return render(request,'staffDashboard.html',{'rentRequests':rentRequests,'exchangeRequests':exchangeRequests})

def detailedExchangeRequest(request, id):
    exchangeRequest = ExchangeRequest.objects.get(id=id)
    return render(request, 'detailedExchangeRequest.html','request':exchangeRequest)