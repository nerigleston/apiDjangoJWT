from django.db import models
from uuid import uuid4


def upload_image_book(instance, filename):
    return f"{instance.id_book}-{filename}"


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    release_year = models.IntegerField()
    state = models.CharField(max_length=100)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to=upload_image_book, null=True, blank=True)
