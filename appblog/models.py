from django.db import models


class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField(primary_key=True)
    nickname=models.CharField(max_length=30)
    email=models.EmailField()
    fecharegistro=models.DateTimeField()

class Libro(models.Model):
    titulo=models.CharField(max_length=80)
    autor=models.CharField(max_length=30)
    genero=models.CharField(max_length=30)
    fechaingreso=models.DateTimeField()

class Comentario(models.Model):
    id=models.IntegerField(primary_key=True)
    creador=models.CharField(max_length=30)
    texto=models.CharField(max_length=5000)
    fechacreación=models.DateTimeField()
