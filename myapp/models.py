from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=timezone.now)
    price = models.IntegerField()
    discription = models.TextField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
