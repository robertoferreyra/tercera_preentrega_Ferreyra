

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "matias_app/index.html")

def cursos(request):
    return render(request, "matias_app/cursos.html")
def profesores(request):
    return render(request, "matias_app/profesores.html")
def estudiantes(request):
    return render(request, "matias_app/estudiantes.html")
def entregables(request):
    return render(request, "matias_app/entregables.html")