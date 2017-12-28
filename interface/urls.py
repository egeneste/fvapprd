from django.conf.urls import url
from .views import *
from django.conf import settings
from django.views.static import serve
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
    url(r'^datos/(?P<modul>[0-9]+)/(?P<temp>[0-9]+)/(?P<hum>[0-9]+)/$', loadDatabase),
    url(r'^notifications/$', notifications),#(?P<bstring>\w+)/(?P<fotostring>[\w.@/+\'-]+)
    url(r'^media/$', alerta, name='alerts'),
    # url(r'^dd/$', loadDatabase)(?P<nic>[0-9]+)
]

if settings.DEBUG :
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]