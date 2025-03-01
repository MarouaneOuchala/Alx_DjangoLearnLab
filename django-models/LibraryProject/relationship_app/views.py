from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Ensure both models are imported

# Function-based view to list all books
def book_list(request):
    Books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Ensure this template exists

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specifies the Library model
    template_name = 'relationship_app/library_detail.html'  # Ensure this template exists
    context_object_name = 'library'  # Use 'library' in the template for easy access