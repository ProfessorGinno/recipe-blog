from django.db import models
from ckeditor import fields

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    # description = fields.RichTextField(max_length=600)
    description = models.CharField(max_length=600)
    image = models.ImageField(upload_to='profile_image', blank=True)
    # creation_date = models.DateTimeField(auto_now_add=True)
    creation_date = models.DateField()
    # actualitation_date = models.DateTimeField(auto_now_add=True)
    actualitation_date = models.DateField()
    recipe_country = models.CharField(max_length=20, blank=True) # Se debe consumir con la API de restcountries.

