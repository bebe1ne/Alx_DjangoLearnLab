from django.contrib import admin
from .models import Book

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year')

# Register your models here.


