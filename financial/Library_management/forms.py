from django import forms
from .models import Book

class bookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'publicationdate',
            'price',
        ]
        
class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100, required=False)       