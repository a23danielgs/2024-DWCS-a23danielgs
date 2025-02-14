from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100,null=True)
    web = models.CharField(max_length=20,null=True)
    role = models.CharField(max_length=20,null=True)
    sign_on = models.CharField(max_length=20,null=True)