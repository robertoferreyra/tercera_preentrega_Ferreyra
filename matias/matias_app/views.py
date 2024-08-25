

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from matias_app.models import Curso
from matias_app.forms import CursoFormulario
from matias_app.forms import BuscaCursoForm , Estudiante, Profesor

def inicio(request):
    return render(request, "matias_app/index.html")


def profesores(request):
    if request.method == "POST":
        mi_formulario = Profesor(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            profesores = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], materia=informacion["materia"])
            profesores.save()

            return render(request, "matias_app/index.html")
    else:
        mi_formulario = Profesor()

    return render(request, "matias_app/profesores.html", {"mi_formulario": mi_formulario})




def cursos(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "matias_app/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "matias_app/cursos.html", {"mi_formulario": mi_formulario})



def estudiantes(request):
    if request.method == "POST":
        mi_formulario = Estudiante(request.POST) 
        if mi_formulario.is_valid:
            informacion = mi_formulario.cleaned_data
            
            estudiantes = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiantes.save()
            return render(request, "matias_app/index.html")
    else:
        mi_formulario = Estudiante()

    return render(request, "matias_app/estudiantes.html", {"mi_formulario": mi_formulario})


def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "matias_app/busqueda.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "matias_app/buscar_form_con_api.html", {"mi_formulario": mi_formulario})