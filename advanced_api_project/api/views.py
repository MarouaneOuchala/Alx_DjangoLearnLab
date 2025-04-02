from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Author model.
    Provides CRUD operations for authors and their related books.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Book model.
    Provides CRUD operations for books with validation.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
