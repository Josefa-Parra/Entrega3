from django.shortcuts import render
from .models import *


def inicio(request):
    return HttpResponse('vista inicio')

def registrarse(request):
    return HttpResponse('vista registrarse')

def crear_viaje(request):
    return HttpResponse('vista crear viaje')

def participar(request):
    return HttpResponse('vista participar')
