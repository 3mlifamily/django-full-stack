from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'description']
