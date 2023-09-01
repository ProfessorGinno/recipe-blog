from django.db import models
from ckeditor import fields
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = fields.RichTextField(max_length=3000)
    image = models.ImageField(upload_to='profile_image', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now_add=True)
    recipe_country = models.CharField(max_length=20, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = fields.RichTextField(max_length=3000)
    created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)