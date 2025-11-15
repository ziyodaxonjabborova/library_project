from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display=['title','status']
    list_filter=['status',]
    search_fields=['title','desc']
