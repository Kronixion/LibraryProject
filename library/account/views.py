from django.shortcuts import render, redirect
from .forms import SignInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Account
from book.models import Book
from django.http import HttpResponse

def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landingPage')
            else:
                form = SignInForm()
                return render(request,'LoginPage.html',{'form':form})
        else:
            form = SignInForm()
            return render(request,'LoginPage.html',{'form':form})
    else:
        form = SignInForm()
        return render(request,'LoginPage.html',{'form':form})

@login_required
def signOut(request):
    logout(request)
    return redirect('/')

@login_required
@csrf_exempt
def shoppingCart(request):
    account = Account.objects.get(id=request.user.id)
    shoppingCart = account.shoppingCart
    if request.method== "POST":
        book = Book.objects.get(id=request.POST['bookId'])
        shoppingCart.books.add(book)
        return HttpResponse("The book "+book.title +" has been added to the shopping cart !")
    else:
        return render(request,'shopping_cart.html',{'shoppingCart':shoppingCart.books.all(),'totalSum':shoppingCart.sumOfBooks(),'totalNumberOfItems':len(shoppingCart.books.all())})