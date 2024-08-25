from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()    

class Estudiantes(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class Profesores(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)

class Entregables(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_de_entrega = forms.DateField()
    entregado = forms.BooleanField()