
from django.urls import path
from matias_app import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('cursos/', views.cursos, name= "Cursos"),
    path('profesores/', views.profesores, name= "Profesores"),
    path('estudiantes/', views.estudiantes, name= "Estudiantes"),
    path('entregables/', views.entregables, name= "Entregables"),
]

clase_21= [
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
    path('form-con-api/', views.form_con_api, name="FormConApi"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]

urlpatterns += clase_21