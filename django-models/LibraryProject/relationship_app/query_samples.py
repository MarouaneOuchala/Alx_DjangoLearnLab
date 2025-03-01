import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Change 'LibraryProject' to your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Corrected query
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"Author '{author_name}' not found."

# Query 2: List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found."

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian.name if library.librarian else "No librarian assigned."
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found."

# Example Usage
if __name__ == "__main__":
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("City Library"))
    print(get_librarian_for_library("City Library"))
