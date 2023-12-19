from django.contrib import admin
from django.urls import path
from appdemanda.views import actor, demandado, expediente, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ),
    path('actor/', actor),
    path('demandado/', demandado),
    path('expediente/', expediente),
    
]
