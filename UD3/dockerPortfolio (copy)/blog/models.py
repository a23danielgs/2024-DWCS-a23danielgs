from django.db import models # type: ignore

class Blog(models.Model):                                
    title = models.CharField(max_length=200)
    description = models.TextField()
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title+f" ({self.id})"