from django.contrib import admin
from django.urls import path
from appdemanda.views import index, formulario_expediente, formulario_actor, formulario_demandado, buscar_actor, buscar_expediente, buscar_demandado, login_request, registro, leerActores, leerDemandados, leerExpedientes, eliminar_actor, eliminar_demandado, eliminar_expediente, editar_actor, editar_demandado, editar_expediente, about, login_request, registro, ActoresLista, DemandadosLista, ExpedientesLista#, eliminar_actor2#,ActoresDetalle, ActoresCrear, ActoresMod, ActoresBorrar
from django.contrib.auth.views import LogoutView


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

    path('leerActores',  leerActores, name = "leerActores"),
    path('leerDemandados',  leerDemandados, name = "leerDemandados"),
    path('leerExpedientes',  leerExpedientes, name = "leerExpedientes"),

    path('eliminar_actor/<actor_apellido>/', eliminar_actor, name="eliminar_actor"),
    #path('eliminar_actor/<actor_id>/', eliminar_actor2, name="eliminar_actor"),
    path('eliminar_demandado/<demandado_apellido>/', eliminar_demandado, name="eliminar_demandado"),
    path('eliminar_expediente/<expediente_numero>/', eliminar_expediente, name="eliminar_expediente"),

    path('editar_actor/<actor_apellido>/', editar_actor, name="editar_actor"),
    path('editar_demandado/<demandado_apellido>/', editar_demandado, name="editar_demandado"),
    path('editar_expediente/<expediente_numero>/', editar_expediente, name="editar_expediente"),

    path('actores_lista', ActoresLista.as_view(), name = "List"),
    path('demandados_lista', DemandadosLista.as_view(), name = "List"),
    path('expedientes_lista', ExpedientesLista.as_view(), name = "List"),
    
    path('about', about, name="about"),

    path('login', login_request, name = "login"),
    path('registro', registro, name = "registro"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name = "logout"),

    #path (r'^(?P<pk>\d+)$', ActoresDetalle.as_view(), name = 'detalle'),
    #path (r'^nuevo$', ActoresCrear.as_view(), name = 'crear'),
    #path (r'^editar/(?P<pk>\d+)$', ActoresMod.as_view(), name = 'editar'),
    #path (r'^borrar(?P<pk>\d+)$', ActoresBorrar.as_view(), name = 'borrar'),
]
