from django.shortcuts import render
from django.http import Http404
from django.db.models import Avg,Min

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    agregation = books.aggregate(Avg("rating"),Min("rating"))

    return render(request,"book_outlet/index.html",{"books":books,"total_number_of_books":num_books,"agregation":agregation})

def book_detail(request,slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling
    })