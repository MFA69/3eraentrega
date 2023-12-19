from django.contrib import admin
from django.urls import path
from appdemanda.views import actor, demandado, expediente, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index" ),
    path('actor/', actor, name = "actor"),
    path('demandado/', demandado, name = "demandado"),
    path('expediente/', expediente, name = "expediente"),
    
]
