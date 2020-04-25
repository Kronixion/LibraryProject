from django.shortcuts import render, redirect
from .forms import SignInForm
from django.contrib.auth import authenticate, login, logout

def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                return render(request,'signIn.html')
        else:
            return render(request,'signIn.html')
    else:
        form = SignInForm()
        return render(request,'signIn.html',{'form':form})

def signOut(request):
    logout(request)
    return redirect('/')