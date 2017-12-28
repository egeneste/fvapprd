from django.shortcuts import render, HttpResponse
# Create your views here.
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import uuid, base64

import socket
import socket



def index(request):

    return render(request, 'realTimeMeters.html')


def lectura(request):
    context = querrys(request, LecturaTempHume)
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
                                 fields=('temperatura', 'tiempo', 'humedad'))
    return HttpResponse(data, 'jjjj.html')

def liveTempHum(request):
    data = serializers.serialize('json', LecturaTempHume.objects.all().order_by('tiempo').reverse(),
                                 fields=('temperatura', 'tiempo', 'humedad'))
    return HttpResponse(data, 'realTimeMeters.html')

def alerta(request):
    context = querrys(request, Alertas)
    return render(request, 'alerts.html', context)

def grafTemp(request):
    return render(request, 'jjjj.html', {})

def loadDatabase(request, modul, temp, hum):

    new_datos = LecturaTempHume()
    new_datos.temperatura = temp
    new_datos.humedad = hum
    new_datos.modulo = modul

    new_datos.save()

    ms = get_object_or_404(Module, modulo='1001')

    if ms.s_temperatura.__eq__("OUT"):
        ms.s_temperatura = 'ON'
        ms.s_humedad = 'ON'

        ms.save()

    return render(request, 'jjjj.html', {})

def notifications(request):

   #  new_not = Alertas()
   # # new_not.modulo = modul
   #  print(id)
   #  if int(id) == 1:
   #      new_not.Tipo = "Sonido"
   #  elif int(id) ==2:
   #      new_not.Tipo = "Humo"
   #  else:
   #      new_not.Tipo = "Sensor Temp/Humedad failed"
   #
   #      # md = get_object_or_404(Module, modulo = '1001')
   #      # md.s_humedad = 'OUT'
   #      # md.s_temperatura = 'OUT'
   #      # md.save()
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serv_addr = (socket.gethostname(), 50000)

    serv.bind(serv_addr)
    serv.listen(1)

   #
   #  connection, client_address = serv.accept()
   #  #data = connection.recv(1024).decode()
   #  filename = str(uuid.uuid4()) + '.png'
   #
   #  # mystring = fotostring[2:]
   #  # mybytes = mystring.encode()#bytes(mystring, 'utf-8')
   #  # with open('media/photos/abc.png', 'wb') as f:
   #  #      f.write(mybytes)#
   #  # new_not.alert_image = 'media/photos/'+filename
   #
   #(?P<modul>[0-9]+)/(?P<id>[0-9]+)/
   # # print(mystring, mybytes)
   #  new_not.save()

    return render(request, 'vacio.html', {'bb': serv_addr})
def querrys(request, modelo):
    print(request.POST.get('startFC'))
    if request.method == "POST":
        if request.POST.get('modulo') !='':
            #request.POST.get('nic')
            print(request.POST)
            querryset = get_object_or_404(modelo, modulo=request.POST.get('modulo'))
            return  {'ob': querryset}

        else:

            try:
                print(request.POST.get('startFC'))

                querrys = modelo.objects.filter(
                    fecha__range=(request.POST.get('startFc'), request.POST.get('endFc')))
                # for ii in querrys:
                #     print(ii.medidor)
                return {'Object_list':  querrys}
            except:
                return {'Object_list': modelo.objects.all()}
        #return {'Object_list': modelo.objects.all()}
    else:
        querryset_list = modelo.objects.all().order_by('tiempo').reverse()
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
            'Object_list': querryset,
            'title': 'Alerta'

        }
        return  context