from django.db import models

class Character(models.Model):                               
    image = models.ImageField(upload_to='Characters/images/')
    alternateImage = models.ImageField(upload_to='Characters/images/',blank=True)
    universe = models.CharField(max_length=100)  
    name = models.CharField(max_length=100)  
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name+f" ({self.id})"