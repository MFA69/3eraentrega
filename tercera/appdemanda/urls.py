from django.contrib import admin
from django.urls import path
from appdemanda.views import index, formulario_expediente, formulario_actor, formulario_demandado, buscar_actor, buscar_expediente, buscar_demandado

urlpatterns = [

    path('', index, name = "index" ),
    path('actor/', formulario_actor, name = "actor"),
    path('demandado/', formulario_demandado, name = "demandado"),
    path('expediente/', formulario_expediente, name = "expediente"),
    path('busqueda_actor_respuesta', buscar_actor, name = "busqueda_actor_respuesta"),
    path('busqueda_demandado_respuesta', buscar_demandado, name = "busqueda_demandado_respuesta"),
    path('busqueda_expediente_respuesta', buscar_expediente, name = "busqueda_expediente_respuesta"),
    path('ingreso_actor', formulario_actor, name='ingreso_actor'),
    path('ingreso_demandado', formulario_demandado, name='ingreso_demandado'),
    path('ingreso_expediente', formulario_expediente, name='ingreso_expediente'),

]
