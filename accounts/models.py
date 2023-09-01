from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)