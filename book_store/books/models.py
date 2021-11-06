
from django.db import models
from django.conf import settings


class Book(models.Model):
    name = models.CharField(max_length=30)
    book_image = models.FileField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    AGE_RANGE = [('18+', 'Adult'), ('<18', 'Adolescent')]
    pg = models.CharField(max_length=3, choices=AGE_RANGE)
