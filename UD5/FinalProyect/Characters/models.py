from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Universe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="universes")
    date_of_creation = models.DateField()
    creator = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="characters")
    universe = models.ForeignKey(Universe,on_delete=models.CASCADE, related_name="characters")
    def __str__(self):
        return f"{self.name}"



