from django.shortcuts import render
from django.http import HttpResponse
from .models import Actor, Demandado, Expediente
from .forms import Formulario_demandado, Formulario_expediente, Formulario_actor

# Create your views here.

def formularioActor (request):
    if request.method == 'POST':
        miformulario = Formulario_actor (request.POST)
        if miformulario.is_valid():
            datos = miformulario.cleaned_data
            print (datos)
            apellido = datos.get("apellido")
            nombre = datos.get("nombre")
            actor = Actor(apellido=apellido,nombre=nombre)
            actor.save()
            return render (request, 'index.html')
    else:
        miformulario = Formulario_actor()

    return render (request, "actor.html", {"miformulario" : miformulario})

def formularioDemandado (request):
    if request.method == 'POST':
        miformulario = Formulario_demandado (request.POST)
        if miformulario.is_valid():
            datos = miformulario.cleaned_data
            print (datos)
            apellido = datos.get("apellido")
            nombre = datos.get("nombre")
            demandado = Demandado(apellido=apellido,nombre=nombre)
            demandado.save()
            return render (request, 'index.html')
    else:
        miformulario = Formulario_demandado()

    return render (request, "demandado.html", {"miformulario" : miformulario})


def formularioExpediente (request):
    if request.method == 'POST':
        miformulario2 = Formulario_expediente (request.POST)
        print(miformulario2)
        if miformulario2.is_valid():
            datos = miformulario2.cleaned_data
            numero = request.POST.get ("numero")
            presentado = request.POST.get ("presentado")
            expediente = Expediente (numero = numero, presentado = presentado)
            expediente.save()
            return render (request, 'index.html')
    else:
        miformulario2 = Formulario_expediente()

    return render (request, "expediente.html", {"miformulario2" : miformulario2})

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
    






#PRACTICA


def actor (request):
    return render (request, "actor.html")

def demandado (request):
    return render (request, "demandado.html")

def expediente (request):
    return render (request, "expediente.html")

def index (request):
    return render (request, "index.html")

def formu_vista (request):

    if request.method == "POST":

        apellido = request.POST.get ("apellido")
        nombre = request.POST.get ("nombre")

        actor = Actor (apellido = apellido, nombre = nombre)
    
        actor.save()

        return render (request, "index.html")

    return render (request, "formulario.html")

def formu2 (request):
    if request.method == 'POST':
        miformulario = Formulario_demandado (request.POST)
        print(miformulario)
        if miformulario.is_valid():
            datos = miformulario.cleaned_data
            apellido = request.POST.get ("apellido")
            nombre = request.POST.get ("nombre")
            demandado = Demandado (apellido = apellido, nombre = nombre)
            demandado.save()
            return render (request, 'index.html')
    else:
        miformulario = Formulario_demandado()

    return render (request, "formu2.html", {"miformulario" : miformulario})


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

    


                   
            



