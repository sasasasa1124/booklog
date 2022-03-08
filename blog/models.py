from re import T
from django.conf import settings
from django.db import models
from django.utils import timezone
from isbn_field import ISBNField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_isbn = ISBNField(clean_isbn=True)
    book_title = models.CharField(max_length=100)
    book_authors = models.CharField(max_length=200, null=True)
    book_publishedDate = models.CharField(max_length=100, null=True)
    book_description = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text