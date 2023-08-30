from django.db import models
from ckeditor import fields
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = fields.RichTextField(max_length=3000)
    # description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='profile_image', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    # creation_date = models.DateField()
    edit_date = models.DateTimeField(auto_now_add=True)
    # edit_date = models.DateField()
    recipe_country = models.CharField(max_length=20, blank=True) # Se debe consumir con la API de restcountries.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = fields.RichTextField(max_length=3000)
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)