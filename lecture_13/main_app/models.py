from django.db import models


# Create your models here.

class Song(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
    )


class Artist(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(to=Song, related_name='artists')


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )


class Review(models.Model):
    description = models.TextField(
        max_length=200,
    )
    rating = models.PositiveIntegerField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='reviews')
