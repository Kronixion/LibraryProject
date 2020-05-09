from django.shortcuts import render,redirect
from account.models import Account
from .models import RentRequest, ExchangeRequest
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import RequestExchangeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail

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
@csrf_exempt
def staffDashboard(request):
    if request.method == "POST":
        if request.POST['requestStatus'] == "Accept":
            rentRequest = RentRequest.objects.get(id=request.POST['id'])
            rentRequest.requestState = 'ACCEPTED'
        else:
            rentRequest = RentRequest.objects.get(id=request.POST['id'])
            rentRequest.requestState = 'REJECTED'
        rentRequest.save()
        return redirect('/staffDashboard/')
    else:
        rentRequests = RentRequest.objects.all()
        exchangeRequests = ExchangeRequest.objects.all()
        return render(request,'staffDashboard.html',{'rentRequests':rentRequests,'exchangeRequests':exchangeRequests})

@login_required
@staff_member_required
@csrf_exempt
def detailedExchangeRequest(request, id):
    exchangeRequest = ExchangeRequest.objects.get(id=id)
    if request.method == "POST":
        if request.POST['requestStatus'] == "Accept":
            send_mail(
                'Booksters - noreply',
                'Your exchange request for the book' + exchangeRequest.book.title + " has been accepted, in exchange for " + exchangeRequest.bookTitle + " ",
                'booksters@wgmail.com',
                [exchangeRequest.user.user.email],
                fail_silently=False,
            )
        else:
            send_mail(
                'Booksters - noreply',
                'Your exchange request for the book' + exchangeRequest.book.title + " has been denied, in exchange for " + exchangeRequest.bookTitle + " ",
                'booksters@wgmail.com',
                [exchangeRequest.user.user.email],
                fail_silently=False,
            )
        ExchangeRequest.objects.get(id=id).delete()
        return redirect('http://localhost:8000/staffDashboard/')
    else:
        print(exchangeRequest.bookImage)
        return render(request, 'detailedExchangeRequest.html',{'request':exchangeRequest})