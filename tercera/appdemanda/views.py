from django.shortcuts import render
from django.http import HttpResponse
from .models import Actor, Demandado, Expediente

# Create your views here.

def actor (request):
    return render (request, "actor.html")

def demandado (request):
    return render (request, "demandado.html")

def expediente (request):
    return render (request, "expediente.html")

def index (request):
    return render (request, "index.html")

