# bookshelf/forms.py

from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import re

class BookForm(forms.ModelForm):
    """Form to create or edit Book instances."""

    class Meta:
        model = Book
        fields = ['title', 'author', 'cover']

    def clean_title(self):
        """Ensure the book title is safe and doesn't contain dangerous characters."""
        title = self.cleaned_data.get('title')
        # Basic validation for dangerous characters
        if re.search(r'[<>\"\'%&]', title):
            raise ValidationError('Title contains invalid characters.')
        return title

    def clean_author(self):
        """Ensure the author's name is safe."""
        author = self.cleaned_data.get('author')
        # Basic validation for dangerous characters
        if re.search(r'[<>\"\'%&]', author):
            raise ValidationError('Author contains invalid characters.')
        return author

    def clean_cover(self):
        """Ensure uploaded cover is a valid image file."""
        cover = self.cleaned_data.get('cover')
        if cover:
            if not cover.name.endswith(('jpg', 'jpeg', 'png', 'gif')):
                raise ValidationError('Invalid file type for cover. Only image files are allowed.')
        return cover
