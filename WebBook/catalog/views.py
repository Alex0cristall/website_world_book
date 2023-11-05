#from cgitb import html
#rom django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Главная страница сайта "World Books"!</h1>')
