# 3eraentrega
Tercera pre-entrega Fernandez Alias


la app tiene 3 clases actor (atributos apellido y nombre), demandado (atributos apellido y nombre) y 
expediente (atributos numero y fecha de presentacion) dentro de models.py

en el archivo views.py creo las funciones, formularioActor, formularioDemandado y formularioExpediente para ingresar datos a la base
y las funciones buscar_actor, buscar_demandado y buscar_expediente para buscar dentro de la base de datos.

desde el nav de la pagina se puede ingresar al contenido de cada una de las clases y volver al index

se puede ingresar por formulario de cada una de las paginas un nuevo actor, un nuevo demandado y un nuevo expediente,
te confirma cada pagina que el ingreso fue exitoso y tiene un boton para volver a la pagina anterior

mas abajo, tambien en su propia pagina, se puede buscar actor, por nombre o apellido, 
se puede buscar demandado por nombre o apellido y se puede buscar un expediente por numero o fecha de presentacion
cada una te lleva a otra pagina con el o los resultados o en su defecto te avisa que no se encontraron resultados,
en todas las opciones tiene un boton para volver a la pagina anterior


