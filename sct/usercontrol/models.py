from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    belongs = models.CharField(max_length=30)
    authority = models.IntegerField(default=2)