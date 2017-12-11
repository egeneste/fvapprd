from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index),
    url(r'^lectura/$', lectura),
    url(r'^modulo/$', modulos),
    url(r'^module-ubucacion/$', moduloUbicacion),
    url(r'^mapa/$', mapa),
    url(r'^area/$',area),
    url(r'^chartTiempo/$',tempVsTiempo)
]