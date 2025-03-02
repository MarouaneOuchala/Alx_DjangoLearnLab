from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """View that allows only users with 'can_view' permission to see books."""
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """View to create a book, restricted to users with 'can_create' permission."""
    if request.method == "POST":
        # Handle book creation logic
        pass
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    """View to edit books, restricted to users with 'can_edit' permission."""
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        # Handle book update logic
        pass
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    """View to delete books, restricted to users with 'can_delete' permission."""
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
