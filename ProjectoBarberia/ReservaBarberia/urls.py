from django.urls import path,include
from .import views

from ReservaBarberia.views import RegistrarBarbero
from ReservaBarberia import views

#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register('ReservaBarberia',views.BarberoList)

app_name = "barberosapp"
urlpatterns = [
    path('registrarbarbero/',RegistrarBarbero.as_view(),name="registrar_barbero"),
    path('barberoslistar/',views.barberos_listado,name="barberos_listado")
]