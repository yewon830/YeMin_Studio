from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=255, unique=True)
    profile_image = models.ImageField(upload_to='porfile_images', null=True, blank=True)
    
    def __str__(self):
        return self.username