from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from useraccount.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.TextField()
    summary = models.TextField()

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.TextField()
    summary = models.TextField()
    rating = models.IntegerField(default=5, validators=[
                                 MinValueValidator(1), MaxValueValidator(5)])
    stock = models.IntegerField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products")
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="products")

    class Meta:
        ordering = ['title', 'created']

    def __str__(self) -> str:
        return self.title
