
from django.urls import path
from matias_app import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('cursos/', views.cursos, name= "Cursos"),
    path('profesores/', views.profesores, name= "Profesores"),
    path('estudiantes/', views.estudiantes, name= "Estudiantes"),
    path('entregables/', views.form_con_api, name= "Entregables"),
]

clase_21= [
    path('form-con-api/', views.form_con_api, name="FormConApi"),
    path('curso_formulario/', views.curso_formulario, name="CursoFormu")
]

urlpatterns += clase_21