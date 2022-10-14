from django.urls import path
from appblog.views import *

urlpatterns = [
    path("", inicio),
    path("bienvenida/", bienvenida, name="entrar"),
    path("user/", user, name="usuario"),
    path("libros/", book, name="libro"),
    path("comentarios/", comment, name="comentario"),
    path("libroFormulario", libroFormulario, name="libroFormulario"),

 ]
    

