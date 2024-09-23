from django.urls import path
from .views import book_list, add_book, search_book, edit_book, delete_book,filter_book_list

urlpatterns = [
    path('',book_list,name='book_list'),
    path('books/add/',add_book,name='add_book'),
    path('books/search/',search_book,name='search_book'),
    path('books/edit/<int:bookID>/',edit_book,name='edit_book'),
    path('books/delete/<int:bookID>/',delete_book,name='delete_book'),
    path('books/filter/',filter_book_list ,name='fillter_book_list'),   
]
