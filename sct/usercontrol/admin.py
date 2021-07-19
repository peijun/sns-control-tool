from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('belongs','authority',)}),)
    list_display = ['username', 'email', 'belongs','authority']


admin.site.register(CustomUser, CustomUserAdmin)