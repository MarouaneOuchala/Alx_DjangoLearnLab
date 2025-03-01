from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library  # Ensure Library model is imported

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/list_books.html'  # Ensure this matches the actual template file
    context_object_name = 'library'  # This allows you to access 'library' in your template
