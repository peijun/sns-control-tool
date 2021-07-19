from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=280)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    image6 = models.ImageField(blank=True)
    image7 = models.ImageField(blank=True)
    image8 = models.ImageField(blank=True)
    image9 = models.ImageField(blank=True)
    image10 = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *arg, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(**arg, **kwargs)

    def __str__(self):
        return self.title
