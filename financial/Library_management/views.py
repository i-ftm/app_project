from django.shortcuts import render, redirect , get_object_or_404
from .models import Book
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json


@csrf_exempt
def add_book(request):
    if request.method == 'post':
        data = json.load(request.body)
        title = data.get('title')
        author = data.get('author')
        price = data.get('price')
        
        book = Book.objects.create(title=title, author=author, price=price)
        return JsonResponse({
            'id': book.pk,
            'title': book.title,
            'author': book.author,
            'price': str(book.price),
            'publication_date': book.publication_date.isoformat()
        }, status=201) #201 = added successfuly
        

def book_list(request):
    books = Book.objects.all()
    book_list = [
        {
            'id' : book.pk ,
            'tittle': book.title,
            'author': book.author,
            'price' : book.price,
            'publicationdate' : book.publicationdate,
        }for book in books]
    
    return JsonResponse({'books': book_list})


def search_book(request):
    query = request.GET.get('query')
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    book_list = [
        {
            'id' : book.pk ,
            'tittle': book.title,
            'author': book.author,
            'price' : book.price,
            'publicationdate' : book.publicationdate,
        }for book in books]
    
    return JsonResponse({'books': book_list})

@csrf_exempt
def edit_book(request , bookID):
    book = get_object_or_404(Book, pk=bookID)
    
    

def delete_book(request , bookID):
    pass

def fillter_book(request):
    pass


# Create your views here.
