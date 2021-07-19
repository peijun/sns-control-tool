from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=280)
    image1 = models.ImageField(upload_to='images',blank=True,null=True)
    image2 = models.ImageField(upload_to='images',blank=True,null=True)
    image3 = models.ImageField(upload_to='images',blank=True,null=True)
    image4 = models.ImageField(upload_to='images',blank=True,null=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
