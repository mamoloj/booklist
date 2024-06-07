from django.db import models

# Create your tests here.
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    # other fields

class Author(models.Model):
    name = models.CharField(max_length=100)
    # other fields

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    pages_written = models.IntegerField()
