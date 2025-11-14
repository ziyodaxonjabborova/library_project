from django.db import models
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    summary = models.TextField(blank=True)
    isbn = models.CharField(max_length=13, blank=True)
    
    def __str__(self):
        return self.title
    

