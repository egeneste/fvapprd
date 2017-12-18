from django.db import models

# Create your models here.
class Module(models.Model):
    modulo = models.CharField(max_length=8, primary_key=True)
    s_state = (
        ('ON', 'ON'),
        ('OFF', 'OFF'),
        ('OUT', 'OUT'),
    )
    s_temperatura   = models.CharField(max_length=5, choices=s_state, default='ON')
    s_humedad       = models.CharField(max_length=5, choices=s_state, default='ON')
    s_sonido        = models.CharField(max_length=5, choices=s_state, default='ON')
    s_humo          = models.CharField(max_length=5, choices=s_state, default='ON')
    latitud         = models.FloatField(blank=True, null=True)
    longitud        = models.FloatField(blank=True, null=True)
    def ubicacion(self):
        link='http://www.google.com/maps/place/%s,%s/@%s,%s' %(self.latitud, self.longitud, self.latitud, self.longitud)
        return str(link)

#
# class Lecture(models.Model):
#     temperatura     = models.FloatField(blank=True, null=True)
#     humedad         = models.FloatField(blank=True, null=True)
#     humo            = models.FloatField(blank=True, null=True)
#     sonido          = models.FloatField(blank=True, null=True)
#     modulo = models.CharField(max_length=8,)

class LecturaTempHume(models.Model):
    temperatura     = models.FloatField(blank=True, null=True)
    humedad         = models.FloatField(blank=True, null=True)
    tiempo       = models.DateTimeField(auto_now=True, )
    modulo = models.CharField(max_length=8)


class ModuloUbicacion(models.Model):
    modulo = models.CharField(max_length=8)
    last_latitud    = models.FloatField(blank=True, null=True)
    last_longitud   = models.FloatField(blank=True, null=True)

    def ubicacion(self):
        link='http://www.google.com/maps/place/%s,%s/@%s,%s' %(self.latitud, self.longitud, self.latitud, self.longitud)
        return str(link)

class Alertas(models.Model):
    modulo = models.CharField(max_length=8, null = True)
    Tipo = models.CharField(max_length= 30, null=True)
    tiempo = models.DateTimeField(auto_now=True, null=True)