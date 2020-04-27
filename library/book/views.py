from django.shortcuts import render
from .models import Book
from .forms import SearchForm

def searchBooks(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            books = Book.objects.filter(title__contains = form.cleaned_data['search'])
            return render(request, 'searchBooks.html',{'form':form,'books':books})
    else:
        books = Book.objects.order_by('title')
        form = SearchForm()
        return render(request, 'searchBooks.html',{'form':form,'books':books})