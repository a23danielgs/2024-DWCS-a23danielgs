from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.caption}"

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts",null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    Author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL,related_name="fkauthor")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    user_name =  models.CharField (max_length=120)
    user_email =  models.EmailField()
    text = models.TextField (max_length=400)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")