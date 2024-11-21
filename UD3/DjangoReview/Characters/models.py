from django.db import models

class Character(models.Model):                                
    image = models.ImageField(upload_to='Characters/images/')
    universe = models.CharField(max_length=100)  
    name = models.CharField(max_length=100)  
    description = models.CharField(max_length=200)   

    def __str__(self):
        return self.title+f" ({self.id})"