# 3eraentrega
Tercera pre-entrega Fernandez Alias

primero clono el repositorio creado en githube en la carpeta 3eraentrega

creo el proyecto con el django-admin startproject tercera

creo la app con el django-admin startapp appdemanda

en models.py creo las tres clases, Actor, Demanda, Expediente

agrego la app en settings.py

me paro en la carpeta de manage.py y pongo el comando python manage.py makemigrations

seguido de python manage.py migrate para crear la base de datos de mis clases

creo en urls.py el path general de path("appdemanda/", include ('appdemanda.urls')),

en el urls.py de la app agrego urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ),
    path('actor/', actor),
    path('demandado/', demandado),
    path('expediente/', expediente),  
]

creo la carpeta templates, y creo los html actor, demandado, expediente

descargo el bootstrap y agrego a la carpeta template el index.html

creo la carpeta static y agrego las carpetas assets, cdd y js

en el archivo views.py creo las funciones, actor, demandado, expediente e index

agrego en el index.html (dentro del head) {% load static %} y <link href="{% static 'css/styles.css' %}" rel="stylesheet" />

