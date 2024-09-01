from django.shortcuts import render, redirect , get_object_or_404
from .models import Book
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
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
        
@csrf_exempt
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

@csrf_exempt
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
    book = get_object_or_404(Book, pk = bookID)
    
    if request.method == 'PUT':
        data = json.loads(request.body)
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.price = data.get('price', book.price)
        book.save()
        
        return JsonResponse({'message': 'Book updated successfully', 'book': {
            'id': book.pk,
            'title': book.title,
            'author': book.author,
            'price': str(book.price),
            'publication_date': book.publication_date.isoformat()
        }})

    return JsonResponse({'error': 'Only PUT requests are allowed'}, status=400)
    

@csrf_exempt
def delete_book(request , bookID):
    book = get_object_or_404(Book, pk = bookID)
    
    if request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book deleted successfully'}, status=204)

    return JsonResponse({'error': 'Only DELETE requests are allowed'}, status=400) 

@csrf_exempt
def fillter_book_list(request):
    books = Book.objects.all()

    price_limit = request.GET.get('price', None)
    if price_limit is not None:
        books = books.filter(price__lte=price_limit)

    publication_date = request.GET.get('publication_date', None)
    if publication_date is not None:
        publication_date = parse_date(publication_date)
        if publication_date:
            books = books.filter(publication_date__gte=publication_date)

    book_list = [{
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'price': str(book.price),
        'publication_date': book.publication_date.isoformat()
    } for book in books]

    return JsonResponse({'books': book_list})


# Create your views here.
