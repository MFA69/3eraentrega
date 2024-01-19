from django.shortcuts import render
from django.http import HttpResponse
from .models import Actor, Demandado, Expediente
from .forms import FormularioDemandado, FormularioExpediente, FormularioActor
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #, UserRegisterForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):
    return render (request, "index.html")

@login_required
def formulario_actor (request):
    if request.method == 'POST':
        miformulario = FormularioActor (request.POST)
        if miformulario.is_valid():
            datos = miformulario.cleaned_data
            apellido = datos.get("apellido")
            nombre = datos.get("nombre")
            actor = Actor(apellido=apellido.title(),nombre=nombre.title())
            actor.save()
            return render (request, 'ingreso_actor.html')
    else:
        miformulario = FormularioActor()

    return render (request, "actor.html", {"miformulario" : miformulario})

@login_required
def formulario_demandado (request):
    if request.method == 'POST':
        miformulario = FormularioDemandado (request.POST)
        if miformulario.is_valid():
            datos = miformulario.cleaned_data
            apellido = datos.get("apellido")
            nombre = datos.get("nombre")
            demandado = Demandado(apellido=apellido.title(),nombre=nombre.title())
            demandado.save()
            return render (request, 'ingreso_demandado.html')
    else:
        miformulario = FormularioDemandado()

    return render (request, "demandado.html", {"miformulario" : miformulario})

@login_required
def formulario_expediente (request):
    if request.method == 'POST':
        miformulario = FormularioExpediente (request.POST)
        if miformulario.is_valid():
            datos = miformulario.cleaned_data
            numero = request.POST.get ("numero")
            presentado = request.POST.get ("presentado")
            expediente = Expediente (numero = numero, presentado = presentado)
            expediente.save()
            return render (request, 'ingreso_expediente.html')
    else:
        miformulario = FormularioExpediente()

    return render (request, "expediente.html", {"miformulario" : miformulario})

def buscar_actor(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre")
        apellido = request.GET.get("apellido")

        if nombre is None and apellido is None:
            return HttpResponse("Debe ingresar al menos un dato válido")

        actor = Actor.objects.filter(
            nombre__icontains=nombre,
            apellido__icontains=apellido
        )

        contexto = {
            "actor": actor,
            "nombre": nombre,
            "apellido": apellido
        }

        return render(request, "busqueda_actor_respuesta.html", contexto)
    
def buscar_demandado(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre")
        apellido = request.GET.get("apellido")

        if nombre is None and apellido is None:
            return HttpResponse("Debe ingresar al menos un dato válido")

        demandado = Demandado.objects.filter(
            nombre__icontains=nombre,
            apellido__icontains=apellido
        )

        contexto = {
            "demandado": demandado,
            "nombre": nombre,
            "apellido": apellido
        }

        return render(request, "busqueda_demandado_respuesta.html", contexto)
    
def buscar_expediente(request):
    if request.method == "GET":
        numero = request.GET.get("numero")
        presentado = request.GET.get("presentado")

        if numero is None and presentado is None:
            return HttpResponse("Debe ingresar al menos un dato válido")

        expediente = Expediente.objects.filter(
            numero__icontains=numero,
            presentado__icontains=presentado
        )

        contexto = {
            "expediente": expediente,
            "numero": numero,
            "presentado": presentado
        }

        return render(request, "busqueda_expediente_respuesta.html", contexto)

#CRUD

def leerActores (request):
     actores = Actor.objects.all()
     contexto = {"actores" : actores}
     return render (request, "leerActores.html", contexto)

def leerDemandados (request):
     demandados = Demandado.objects.all()
     contexto = {"demandados" : demandados}
     return render (request, "leerDemandados.html", contexto)

def leerExpedientes (request):
     expedientes = Expediente.objects.all()
     contexto = {"expedientes" : expedientes}
     return render (request, "leerExpedientes.html", contexto)

@login_required
def eliminar_actor (request, actor_apellido):
    actor = Actor.objects.get(apellido=actor_apellido)
    actor.delete()
    actores = Actor.objects.all()
    contexto = {"actores": actores}
    return render (request, "leerActores.html", contexto)

@login_required
def eliminar_demandado (request, demandado_apellido):
    demandado = Demandado.objects.get(apellido=demandado_apellido)
    demandado.delete()
    demandados = Demandado.objects.all()
    contexto = {"demandados": demandados}
    return render (request, "leerDemandados.html", contexto)

@login_required
def eliminar_expediente (request, expediente_numero):
    expediente = Expediente.objects.get(numero=expediente_numero)
    expediente.delete()
    expedientes = Expediente.objects.all()
    contexto = {"expedientes": expedientes}
    return render (request, "leerExpedientes.html", contexto)

@login_required
def editar_actor (request, actor_apellido):

    actor = Actor.objects.get(apellido=actor_apellido)

    if request.method == 'POST':

        miformulario = FormularioActor (request.POST)

        if miformulario.is_valid():

            datos = miformulario.cleaned_data
            actor.apellido = datos['apellido']
            actor.nombre = datos['nombre']
            actor.save()
            #return render (request, "leerActores.html")
            #return render (request, 'editar_actor.html')
            return render (request, "actores_lista.html")
    else:
        miformulario = FormularioActor(initial={'apellido': actor.apellido, 'nombre': actor.nombre})

    return render (request, "editar_actor.html", {"miformulario" : miformulario, 'actor_apellido': actor_apellido})
    
@login_required   
def editar_demandado (request, demandado_apellido):

    demandado = Demandado.objects.get(apellido=demandado_apellido)

    if request.method == 'POST':

        miformulario = FormularioDemandado (request.POST)

        if miformulario.is_valid():

            datos = miformulario.cleaned_data
            demandado.apellido = datos['apellido']
            demandado.nombre = datos['nombre']
            demandado.save()
            #return render (request, "leerActores.html")
            #return render (request, 'editar_actor.html')
            return render (request, "demandados_lista.html")
    else:
        miformulario = FormularioDemandado(initial={'apellido': demandado.apellido, 'nombre': demandado.nombre})

    return render (request, "editar_demandado.html", {"miformulario" : miformulario, 'demandado_apellido': demandado_apellido})

@login_required
def editar_expediente (request, expediente_numero):

    expediente = Expediente.objects.get(numero=expediente_numero)

    if request.method == 'POST':

        miformulario = FormularioExpediente (request.POST)

        if miformulario.is_valid():

            datos = miformulario.cleaned_data
            expediente.numero = datos['numero']
            expediente.presentado = datos['presentado']
            expediente.save()
            #return render (request, "leerActores.html")
            #return render (request, 'editar_actor.html')
            return render (request, "expedientes_lista.html")
    else:
        miformulario = FormularioExpediente(initial={'numero': expediente.numero, 'presentado': expediente.presentado})

    return render (request, "editar_expediente.html", {"miformulario" : miformulario, 'expediente_numero': expediente_numero})

#class view
class ActoresLista (ListView):
    model = Actor
    template_name = 'actores_lista.html'

class DemandadosLista (ListView):
    model = Demandado
    template_name = 'demandados_lista.html'

class ExpedientesLista (ListView):
    model = Expediente
    template_name = 'expedientes_lista.html'

#about

def about (request):
    return render (request, "about.html")

#login

def login_request (request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login (request, user)

                return render (request, "index.html", {"mensaje" : f"Registro de usuario {username} exitoso"})
            
            else:

                return render (request, "index.html", {"mensaje" : f"Error usuario o contraseña para registrarse"})
            
        else:

            return render (request, "index.html", {"mensaje" : f"Usuario o contraseña erroneos"})

    form = AuthenticationForm()

    return render (request, "login.html", {"form" : form})

def registro (request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get("username")

            form.save()

            return render (request, 'index.html', {"mensaje": f"Usuario {username} creado"})
 
    else:
        form = UserCreationForm()

    return render (request, 'registro.html', {'form': form})
   
#PRACTICA 2

def eliminar_actor2 (request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    actor.delete()
    actores = Actor.objects.all()
    contexto = {"actores": actores}
    return render (request, "leerActores.html", contexto)


#class ActoresDetalle (DetailView):
 #   model = Actor
  #  template_name = 'actores_detalle.html'

#class ActoresCrear (CreateView):
 #   model = Actor
  #  success_url = 'leerActores.html'
   # fields = ['apellido', 'nombre']

#class ActoresMod (UpdateView):
 #   model = Actor
  #  success_url = 'leerActores.html'
   # fields = ['apellido', 'nombre']

#class ActoresBorrar (DeleteView):
 #   model = Actor
  #  success_url = 'leerActores.html'




#PRACTICA


#def actor (request):
 #   return render (request, "actor.html")

#def demandado (request):
    #return render (request, "demandado.html")

#def expediente (request):
    #return render (request, "expediente.html")



#def formu_vista (request):

    #if request.method == "POST":

      #  apellido = request.POST.get ("apellido")
      #  nombre = request.POST.get ("nombre")

       # actor = Actor (apellido = apellido, nombre = nombre)
    
       # actor.save()

      #  return render (request, "index.html")

    #return render (request, "formulario.html")

#def formu2 (request):
   # if request.method == 'POST':
       # miformulario = Formulario_demandado (request.POST)
       # print(miformulario)
       # if miformulario.is_valid():
          #  datos = miformulario.cleaned_data
          #  apellido = request.POST.get ("apellido")
          #  nombre = request.POST.get ("nombre")
          #  demandado = Demandado (apellido = apellido, nombre = nombre)
         #   demandado.save()
         #   return render (request, 'index.html')
    #else:
       # miformulario = Formulario_demandado()

   # return render (request, "formu2.html", {"miformulario" : miformulario})


#FUNCIONO
# def buspru(request):
    #if request.method == 'GET':
        #nombre = request.GET.get("nombre")

        #if nombre is None:
            #return HttpResponse (f"datos erroneos")
        
        #actor = Actor.objects.filter(nombre__icontains=nombre)

        #contexto = {
            #"actor" : actor,
            #"nombre" : nombre
        #}

        #return render (request, "prbu.html", contexto)

#FUNCIONO!!!
 
#def prueba_busqueda (request):
    #if request.method == 'GET':

       # nombre = request.GET.get("nombre")

        #print (f"vamos a buscar el actor: {nombre}")

    #return render (request, "pruebabusqueda.html")

#def busqueda_actor(request):
    #if request.method == "GET":
        #nombre = request.GET.get("nombre")
        #return HttpResponse (f"estamos buscando el actor: {nombre}")

        #return render(request, 'busquedaActor.html')
        #return render(request, 'actor.html')

#def buscar(request):
    #respuesta = f"estoy buscando al actor: {request.GET['actor']}"

    #return HttpResponse (respuesta)

#def buscar(request):
    #if request.GET["nombre"]:
        #nombre = request.GET["nombre"]
        #nombre = Actor.object.filter(nombre__icontains=nombre)

        #return render (request, "busqueda_actor_respuesta.html", {"actor" : actor, "nombre" : nombre})
    
    #else: 
        #respuesta= "no enviaste datos"

        #return HttpResponse (respuesta)

    


                   
            



