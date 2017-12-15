from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^lectura/$', lectura),
    url(r'^modulo/$', modulos),
    url(r'^module-ubucacion/$', moduloUbicacion),
    url(r'^mapa/$', mapa),
    url(r'^area/$',area),
    url(r'^chartTiempo/$',tempVsTiempo),
    url(r'^liveth/$',liveTempHum),
    url(r'^grafica-temperatura-vs-tiempo/$', grafTemp),
   # url(r'^articles/([0-9]{4})/([0-9]{5})/([0-9]+)/$', loadDatabase),
    url(r'^datos/(?P<modul>[0-9]{4})/(?P<temp>[0-9]{2})/(?P<hum>[0-9]{2})/$', loadDatabase),
    # url(r'^dd/$', loadDatabase)
]