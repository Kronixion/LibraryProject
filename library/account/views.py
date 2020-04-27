from django.shortcuts import render, redirect
from .forms import SignInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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

def signOut(request):
    logout(request)
    return redirect('/')

@login_required
def shoppingCart(request):
    return render(request,'shopping_cart.html')