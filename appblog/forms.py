from socket import fromshare
from django import forms



class LibroFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    genero = forms.CharField()
    fechaingreso = forms.DateField()
    
    