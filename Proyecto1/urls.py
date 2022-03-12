from ctypes.wintypes import HLOCAL
from django.contrib import admin
from django.urls import path
from Proyecto1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diaActual/', diaDeHoy),
    path('Nombre/<nombre>', miNombreEs),
    path('Template/', probandoTemplate)
    
]


