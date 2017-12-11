from django.contrib import admin
from .models import *
# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('modulo', 's_temperatura', 's_humedad', 's_humo', 's_sonido')

admin.site.register(Module, ModuleAdmin)