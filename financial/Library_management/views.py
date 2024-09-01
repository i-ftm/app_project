from django.shortcuts import render, redirect , get_object_or_404
from .models import book
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def add_book(request):
    pass

def book_list(request):
    books_list = book.object.all()
    return render(request,)

def search_book(request):
    pass

def edit_book(request):
    pass

def delete_book(request):
    pass

def fillter_book(request):
    pass


# Create your views here.
