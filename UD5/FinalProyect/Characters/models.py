from django.db import models
from django.core.validators import MinLengthValidator
from Characters.templatetags.slugify_filters import slugify_filter


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
    
    def save(self, *args, **kwargs):
        if not self.slug or self._state != 'adding' and self.name != Universe.objects.get(id=self.id).name:  
            base_slug = slugify_filter(self.name)
            self.slug = base_slug
        super().save(*args, **kwargs)
    
class Character(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="characters")
    alternateImage = models.ImageField(upload_to="characters",blank=True)
    universe = models.ForeignKey(Universe,on_delete=models.CASCADE, related_name="characters")
    slug = models.SlugField(unique=True,db_index=True)
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.slug or self._state != 'adding' and self.name != Character.objects.get(id=self.id).name:
            base_slug = slugify_filter(self.name)
            self.slug = base_slug
        super().save(*args, **kwargs)




