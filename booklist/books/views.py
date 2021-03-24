from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DetailView,
    DeleteView,
)

from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    
    
