from django.db import models

# Create your models here.

class course(models.Model):
    name = models.CharField(max_length=100)
    long_description = models.CharField(max_length=99999)
    photo = models.ImageField(upload_to='courses/images/')