from django.contrib import admin
from django.urls import path
from appdemanda.views import index, formularioExpediente, formularioActor, formularioDemandado, buscar_actor, buscar_expediente, buscar_demandado

urlpatterns = [

    path('', index, name = "index" ),
    path('actor/', formularioActor, name = "actor"),
    path('demandado/', formularioDemandado, name = "demandado"),
    path('expediente/', formularioExpediente, name = "expediente"),
    path('busqueda_actor_respuesta', buscar_actor, name = "busqueda_actor_respuesta"),
    path('busqueda_demandado_respuesta', buscar_demandado, name = "busqueda_demandado_respuesta"),
    path('busqueda_expediente_respuesta', buscar_expediente, name = "busqueda_expediente_respuesta"),

]
