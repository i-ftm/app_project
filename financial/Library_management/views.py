from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Book
from .forms import bookForm 
from .forms import SearchForm
from django.contrib import messages
from django.db.models import Q 


def book_list(request):
    books = Book.objects.all()
    
    return render(
        request,
        'book_list.html',
        {'books':books}
    )


def add_book(request):
    form = bookForm()
    
    if request.method == 'POST':
        form = bookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Book added successfully'
            )
            
            return redirect(
                'book_list'
            )

    return render(
        request,
        'add_book.html',
        {'form': form}
    )
    

def search_book(request):
    search_form = SearchForm(request.GET)
    books = Book.objects.all()
    if search_form.is_valid() and search_form.cleaned_data['query']:
        search_item = search_form.cleaned_data['query']
        books = books.filter(
            Q(title__icontains = search_item) |
            Q(author__icontains = search_item)
        )
        
    return render(
        request,
        'book_list.html',
        {
            'books':books ,
            'search_form': search_form,
        }
    )


def edit_book(request , bookID):
    book = get_object_or_404(Book, id = bookID)
    
    if request.method == 'POST':
        form = bookForm(request.POST, instance=book)
        if form.is_valid():
            book.save()
            return redirect('book_list')
    else:
        form = bookForm(instance=book)  

    return render(
        request,
        'edit_book.html',
        {'form': form, 'book': book},
    )



def delete_book(request , bookID):
    book = get_object_or_404(Book, id = bookID)
    book.delete()
    return redirect('book_list')


def filter_book_list(request):
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    publication_date = request.GET.get('publication_date')

    books = Book.objects.all()
    
    if price_min:
        books = books.filter(price__gte=price_min)
    if price_max:
        books = books.filter(price__lte=price_max)
    if publication_date:
        books = books.filter(publication_date=publication_date)

    return render(
        request,
        'filter_books.html',
        {'books': books},
    )
