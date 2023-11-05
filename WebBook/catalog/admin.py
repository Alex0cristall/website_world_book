from django.contrib import admin
from .models import Book, Language, Gener, Author, Status, BookInstance, Publisher

# Register your models here.

admin.site.register(Author)
admin.site.register(Gener)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
admin.site.register(BookInstance)
