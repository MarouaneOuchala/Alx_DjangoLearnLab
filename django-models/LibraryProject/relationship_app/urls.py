from django.urls import path
from .views import list_books  # Import the views

urlpatterns = [
    path('books/', book_list, name='book_list'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
]
