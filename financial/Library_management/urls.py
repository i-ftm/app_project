from django.urls import path
from .views import *

urlpatterns = [
    path('api/books/',book_list,name='book_list'),
    path('api/books/add/',add_book,name='add_book'),
    path('api/books/search/',search_book,name='search_book'),
    path('api/books/edit/<int:bookID>/',edit_book,name='edit_book'),
    path('api/books/delete/<int:bookID>/',delete_book,name='delete_book'),
    path('api/books/filter/',fillter_book_list,name='fillter_book_list'),
    
]
