# from cgitb import html
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import context
from .models import Book, Author, BookInstance
from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    """Словарь для передачи данных в шаблон"""
    text_head = 'Главная страница сайта "World Books"!'

    """Данные о книгах и их количестве"""
    books = Book.objects.all()
    count_all_books = Book.objects.all().count()

    """Данные об экземплярах книг в БД"""
    count_all_instances = Book.objects.all().count()

    """Доступные книги (статус = 'На складе')"""
    count_instances_available = BookInstance.objects.filter(status__exact=1).count()

    """Данные об авторах книг"""
    author = Author.objects
    count_all_authors = Author.objects.count()
    

    """Словарь для передачи данных в шаблон index.htm"""
    contexts = {
        "text_head": text_head,
        "books": books,
        "count_all_books": count_all_books,
        "count_all_instances": count_all_instances,
        "count_instances_available": count_instances_available,
        "author": author,
        "count_all_authors": count_all_authors,
    }

    return render(request, "catalog/index.html", context=contexts)


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 5


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book' # --- поумочанию  равен objects
    #template_name = 'detail_book.html' # --- здаётся html шаблон



