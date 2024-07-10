from django.urls import path
from AppViajes import views

urlspatterns = [
    path('',views.inicio),
    path('registrarse',views.registrarse, name="Registrarse"),
    path('crear viaje',views.crear_viaje),
    path('participar',views.participar),

]