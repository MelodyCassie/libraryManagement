from uuid import uuid4

from django.db import models
from django.conf import settings


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    POLITICS = "P"
    FINANCE = "F"
    ROMANCE = "R"

    BOOK_CHOICES = [
        (POLITICS, 'politics'),
        (FINANCE, 'Finance'),
        (ROMANCE, 'Romance'),
    ]
    title = models.TextField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=20)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    # review = models.ManyToOneRel(o,'Review')

    def __str__(self):
        return f"{self.title} {self.isbn} "

    def list_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:2])


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class BookInstance(models.Model):
    AVAILABLE = "A"
    UNAVAILABLE = "U"
    LOAN_CHOICES = [
        (UNAVAILABLE, "Unavailable"),
        (AVAILABLE, "Available"),
    ]
    unique_id = models.UUIDField(default=uuid4, primary_key=True)
    due_back = models.DateTimeField()
    status = models.CharField(max_length=1, choices=LOAN_CHOICES, default=AVAILABLE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.status} {self.due_back} {self.borrower}"


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
