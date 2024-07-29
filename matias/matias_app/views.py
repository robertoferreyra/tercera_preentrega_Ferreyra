

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from matias_app.models import Curso
from matias_app.forms import CursoFormulario
from matias_app.forms import BuscaCursoForm

def inicio(request):
    return render(request, "matias_app/index.html")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")

def curso_formulario(request):

    if request.method == 'POST':

        curso = Curso(nombre=request.POST['curso'],camada=request.POST['camada'])
        curso.save()

        return render(request, "matias_app/index.html")

    return render(request,"matias_app/curso_formulario.html")


def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "matias_app/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "matias_app/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "matias_app/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "matias_app/buscar_form_con_api.html", {"mi_formulario": mi_formulario})