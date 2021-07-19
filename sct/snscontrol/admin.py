from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content','image1']

admin.site.register(Post, PostAdmin)