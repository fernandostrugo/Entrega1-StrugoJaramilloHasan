from django.http import HttpResponse
from django.shortcuts import render
from appblog.models import *
from appblog.forms import LibroFormulario

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

def libroFormulario(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro (titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"], fechaingreso=informacion["fechaingreso"])
            libro.save()
            return render(request, "appblog/index.html")
    else:
            
     miFormulario = LibroFormulario()
        
    return render(request, "appblog/libroFormulario.html", {"miFormulario":miFormulario})
