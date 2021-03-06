from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=280)
    image1 = models.ImageField(upload_to="images", blank=True, null=True)
    image2 = models.ImageField(upload_to="images", blank=True, null=True)
    image3 = models.ImageField(upload_to="images", blank=True, null=True)
    image4 = models.ImageField(upload_to="images", blank=True, null=True)
    is_public = models.BooleanField(default=False)
    public_time = models.DateTimeField(blank=True, null=True)
    is_publish_twitter = models.BooleanField(default=False)
    is_publish_instagram = models.BooleanField(default=False)
    is_publish_facebook = models.BooleanField(default=False)
    is_publish_line = models.BooleanField(default=False)
    is_approval = models.BooleanField(default=False)
    approver = ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
