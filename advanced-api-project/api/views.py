from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing author instances.
    Provides standard CRUD operations and additional custom actions.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk=None):
        """
        Custom endpoint to get statistics about an author's books.
        Returns the total number of books and the range of publication years.
        """
        author = self.get_object()
        books = author.books.all()
        
        if not books.exists():
            return Response({
                'total_books': 0,
                'publication_years': None
            })

        years = books.values_list('publication_year', flat=True)
        return Response({
            'total_books': len(books),
            'publication_years': {
                'earliest': min(years),
                'latest': max(years)
            }
        })

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing book instances.
    Provides standard CRUD operations with filtering and search capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']

    def get_queryset(self):
        """
        Optionally restricts the returned books by filtering against
        query parameters in the URL.
        """
        queryset = super().get_queryset()
        year = self.request.query_params.get('year', None)
        
        if year is not None:
            queryset = queryset.filter(publication_year=year)
        
        return queryset
