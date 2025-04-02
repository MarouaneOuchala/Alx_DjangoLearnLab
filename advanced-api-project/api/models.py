from django.db import models

class Author(models.Model):
    """
    Model representing an author of books.
    This model stores basic information about authors and has a one-to-many
    relationship with books through the related_name='books'.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    This model stores information about books and maintains a relationship
    with their respective authors through a foreign key.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        help_text='The author who wrote this book'
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year}) by {self.author.name}"

    class Meta:
        ordering = ['-publication_year']
