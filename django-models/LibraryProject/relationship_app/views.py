from django.shortcuts import render
from .models import Book  # Ensure you have the Book model

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})  # Ensure the correct template name
