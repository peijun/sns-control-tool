from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "content",
        "image1",
        "image2",
        "image3",
        "image4",
        "is_public",
        "is_approval",
    ]


admin.site.register(Post, PostAdmin)
