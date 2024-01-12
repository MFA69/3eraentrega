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

#class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    #password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
   # password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    #class Meta:
       #  fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
       # help_texts = {k:"" for k in fields}



#SIN USO

class BusquedaActor(forms.Form):
    #apellido = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)