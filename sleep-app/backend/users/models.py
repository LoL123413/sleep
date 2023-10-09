from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)
    
class Category(models.Model):
    name = models.CharField(max_length=255)

#parent model

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
    
