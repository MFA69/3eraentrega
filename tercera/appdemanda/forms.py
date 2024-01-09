from django import forms


class FormularioActor(forms.Form):
    apellido = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)

class FormularioDemandado(forms.Form):
    apellido = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)

class FormularioExpediente(forms.Form):
    numero = forms.IntegerField()
    presentado = forms.DateField()


#SIN USO

class BusquedaActor(forms.Form):
    #apellido = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)