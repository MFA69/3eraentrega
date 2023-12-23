from django import forms


class Formulario_actor(forms.Form):
    apellido = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)

class Formulario_demandado(forms.Form):
    apellido = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)

class Formulario_expediente(forms.Form):
    numero = forms.IntegerField()
    presentado = forms.DateField()

class Busqueda_actor(forms.Form):
    #apellido = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)