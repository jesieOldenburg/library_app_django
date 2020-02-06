from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):
    """Model definition for Book."""

    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Book."""

        verbose_name = ('Book')
        verbose_name_plural = ('Books')

    def __str__(self):
        """Unicode representation of Book."""
        pass
    