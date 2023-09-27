from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title