from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Degree(models.Model):
 name = models.CharField(max_length=100)
 description = models.CharField(max_length=250)
 number_of_years = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

class Student(models.Model):
    name_surname = models.CharField(max_length=100)
    picture = models.ImageField()
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(54)])
    slug = models.SlugField(default="", null=False, db_index=True, unique=True) 
    finished_degree = models.BooleanField()
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True, related_name="fkstudents")

    def get_absolute_url(self):
        return reverse("student-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_surname)
        super().save(*args, **kwargs)

    def __str__(self):
       return f"{self.name_surname}"