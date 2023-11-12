import imp
from django.contrib import admin
from django.templatetags.i18n import language
from django.utils.html import format_html

from .models import Book, Language, Gener, Author, Status, BookInstance, Publisher


# Register your models here.

# admin.site.register(Author)
# admin.site.register(Gener)
# admin.site.register(Book)
# admin.site.register(Language)
# admin.site.register(Publisher)
# admin.site.register(Status)
# admin.site.register(BookInstance)




# Определяем в клласе AuthorAdmin для авторов книг
class AuthorAdmin(admin.ModelAdmin):
    ''' Порядок расположения полей -- (list_display = tuple(...)) '''
    list_display = ('last_name', 'first_name', 'surname', 'photo')#, 'show_photo')

    ''' Порядок расположения полей ввода данных, (то что в картеже выведится в одной строке) 
        вместо fields можно использовать exclude -- позволяет исключать поля '''
    fields = ['last_name', 'first_name', 'surname', ('date_of_birth', 'photo')]


    #readonly_fields = ['show_photo']
    # def show_photo(self, obj):
    #     return format_html(
    #         f'<img src="{obj.photo.url}" style="height: 100px;">')
    # show_photo.short_description = 'Фото'


# Регистрируем к.ласе AuthorAdmin для авторов книг
admin.site.register(Author, AuthorAdmin)




class BookInstanceInline(admin.TabularInline):
    ''' Позволяет в поле редактирование просматривать сразу несколько моделей '''
    model = BookInstance


# Регистрируем к.ласе BookAdmin для книг
@admin.register(Book)  # декоратор идеинтичен admin.site.register(...)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'gener', 'language', 'display_author', 'show_photo')
    ''' Добавление фильтра поиска '''
    list_filter = ('gener', 'author')


    inlines = [BookInstanceInline]


    readonly_fields = ['show_photo']
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo_url}" style="max-height: 100px;">')
    
    show_photo.short_description = 'Фото'




@admin.register(BookInstance)  # декоратор идеинтичен admin.site.register(...)
class BookInstanceAdmin(admin.ModelAdmin):
    ''' Добавление фильтра поиска '''
    list_filter = ('book', 'status')

    ''' Делит страницу на секции с возможностью озоглавить '''
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'inv_nom')
        }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back')
        })
    )





admin.site.register(Gener)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
