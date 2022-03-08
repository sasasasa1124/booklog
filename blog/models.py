from re import T
from django.conf import settings
from django.db import models
from django.utils import timezone
from isbn_field import ISBNField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_isbn = ISBNField(clean_isbn=True)
    book_title = models.CharField(max_length=200)
    book_authors = models.CharField(max_length=200)
    book_publishedDate = models.DateTimeField(default=timezone.now)
    book_description = models.CharField(max_length=1000)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return self.title
