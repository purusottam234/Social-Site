from django.contrib import admin
from .models import images

# Register your models here.


@admin.register(images)
class imagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
