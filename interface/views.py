from django.shortcuts import render, HttpResponse
# Create your views here.
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import json
from django.http import HttpResponse
from django.http import JsonResponse
def index(request):

    return render(request, 'realTimeMeters.html')


def lectura(request):

    querryset_list = LecturaTempHume.objects.all()
    paginator = Paginator(querryset_list, 15)
    page = request.GET.get('page')
    try:
        querryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        querryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        querryset = paginator.page(paginator.num_pages)

    context = {
        'Object_list': querryset

    }
    return render(request, 'lecture.html', context)


def moduloUbicacion(request):
    querryset_list = ModuloUbicacion.objects.all()
    paginator = Paginator(querryset_list, 15)
    page = request.GET.get('page')
    try:
        querryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        querryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        querryset = paginator.page(paginator.num_pages)

    context = {
        'Object_list': querryset

    }
    return render(request, 'moduloUbicacion.html', context)


def modulos(request):
    querryset_list = Module.objects.all()
    paginator = Paginator(querryset_list, 15)
    page = request.GET.get('page')
    try:
        querryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        querryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        querryset = paginator.page(paginator.num_pages)

    context = {
        'Object_list': querryset

    }
    return render(request, 'modulo.html', context)

def mapa(request):

    data = serializers.serialize('json', Module.objects.all(), fields=('modulo', 's_temperatura', 's_humedad', 's_sonido', 's_humo', 'latitud', 'longitud'))

    return HttpResponse(data, 'mapa.html')


def area(request):
    return render(request, 'mapa.html', {})

def tempVsTiempo(request):
    data = serializers.serialize('json', LecturaTempHume.objects.all(),
                                 fields=('temperatura', 'timestamp', 'humedad'))
    return HttpResponse(data, 'jjjj.html')

def grafTemp(request):
    return render(request, 'jjjj.html', {})

def loadDatabase(request, modul, temp, hum):

    new_datos = LecturaTempHume()
    new_datos.temperatura = temp
    new_datos.humedad = hum
    new_datos.modulo = modul

    new_datos.save()

    return render(request, 'jjjj.html', {})
