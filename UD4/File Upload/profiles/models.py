from django.db import models



# MODELS :



class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")