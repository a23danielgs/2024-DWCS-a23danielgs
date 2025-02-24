from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Universe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="universes")
    date_of_creation = models.DateField()
    creator = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,db_index=True)
    def __str__(self):
        return f"{self.name}"
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="characters")
    alternateImage = models.ImageField(upload_to="characters",blank=True)
    universe = models.ForeignKey(Universe,on_delete=models.CASCADE, related_name="characters")
    slug = models.SlugField(unique=True,db_index=True)
    def __str__(self):
        return f"{self.name}"



