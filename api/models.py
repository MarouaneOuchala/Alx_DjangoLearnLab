from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Model representing an author.
    
    Fields:
        name (CharField): The name of the author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model representing a book.
    
    Fields:
        title (CharField): The title of the book.
        publication_year (IntegerField): The year the book was published.
        author (ForeignKey): Reference to the Author model, establishing a one-to-many relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        ordering = ['publication_year']

    def __str__(self):
        return self.title
