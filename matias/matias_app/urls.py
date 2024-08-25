
from django.urls import path
from matias_app import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('cursos/', views.cursos, name= "Cursos"),
    path('profesores/', views.profesores, name= "Profesores"),
    path('estudiantes/', views.estudiantes, name= "Estudiantes"),
    path('Busqueda/', views.buscar_form_con_api, name= "Busqueda"),
]

clase_21= [

]

urlpatterns += clase_21