from django.http import HttpResponse
from django.shortcuts import render
from appblog.models import *

def inicio(request):
     return render(request, "appblog/index.html")

def bienvenida(request):
    return render(request, "appblog/bienvenida.html")

def user(request):
    users= Usuario.objects.all()
    return render(request, "appblog/usuarios.html",{'users':users})


def book(request):
    books= Libro.objects.all()
    return render(request, "appblog/libros.html",{'books':books})

def comment(request):
    comments= Comentario.objects.all()
    return render(request, "appblog/comentarios.html",{'comments':comments})

