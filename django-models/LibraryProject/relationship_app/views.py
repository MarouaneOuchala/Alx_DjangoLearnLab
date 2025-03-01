from django.shortcuts import render
from .models import Book  # Ensure you have the Book model

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Ensure the correct template name
