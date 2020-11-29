from django.contrib import admin
from .models import *


class BaseComputadoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'formato', 'procesador', 'memoria', 'disco', 'sistema_operativo', 'cambio_pasta', 'estado', 'notas')
    list_filter = ('estado',)

class OcultarModeloAdmin(admin.ModelAdmin): 
    def get_model_perms(self, request):
        return {}

admin.site.register(Computadora, BaseComputadoraAdmin)
admin.site.register(Microprocesador, OcultarModeloAdmin)
admin.site.register(TarjetaMemoriaRam, OcultarModeloAdmin)
admin.site.register(DiscoRigido, OcultarModeloAdmin)
admin.site.register(SistemaOperativo, OcultarModeloAdmin)

