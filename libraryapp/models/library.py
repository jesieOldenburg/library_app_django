from django.db import models

class Library(models.Model):
    """Model definition for Library."""

    # TODO: Define fields here
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        """Meta definition for Library."""

        verbose_name = 'Library'
        verbose_name_plural = 'Librarys'

    def __str__(self):
        """Unicode representation of Library."""
        pass
