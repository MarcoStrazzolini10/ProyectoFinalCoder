from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

def nosotros(request):
    return render(request, "paginas/inicio.html")

def nosotros(request):
    return render(request, "paginas/nosotros.html")

def Libros(request):
    Libros = Libros.object.all()
    return render(request, "Libros/index.html")

def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render{request, "Libros/crear.html", {'formulario' : formulario }}

def editar(request,id):
    libro = Libro.objects.get(id=id)
    return render(request, "Libros/editar.html", {'formulario': formulario })

def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    Libro.delete()
    return redirect("Libros")