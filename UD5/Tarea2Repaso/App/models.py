from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='images/')
    slug = models.SlugField(default="", null=False, db_index=True, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name="fkproduct")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)