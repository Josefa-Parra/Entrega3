from django.db import models

class Registrarse(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    ciudad= models.CharField(max_length=40)
                                                      
class Crear_Viaje(models.Model):
    nombre_tutor= models.CharField(max_length=40)
    lugar= models.CharField(max_length=40)
    dia= models.DateField()
    hora= models.CharField(max_length=40)
    ciudad= models.CharField(max_length=40)
    codigo_viaje= models.CharField(max_length=40)

class Participar(models.Model):
    codigo_viaje= models.CharField(max_length=40)
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()