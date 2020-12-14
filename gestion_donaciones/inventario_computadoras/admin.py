from django.contrib import admin
from .models import Computadora, Microprocesador, TarjetaMemoriaRam, DiscoRigido, SistemaOperativo

admin.site.site_header = "APP administración ATSV"


@admin.register(Computadora)
class ComputadoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'formato', 'procesador', 'memoria', 'disco', 'sistema_operativo', 'cambio_pasta', 'estado', 'notas')
    list_filter = ('estado',)


@admin.register(Microprocesador)
class MicroprocesadorAdmin(admin.ModelAdmin):
    pass


@admin.register(TarjetaMemoriaRam)
class TarjetaMemoriaRamAdmin(admin.ModelAdmin):
    pass


@admin.register(DiscoRigido)
class DiscoRigidoAdmin(admin.ModelAdmin):
    pass


@admin.register(SistemaOperativo)
class SistemaOperativoAdmin(admin.ModelAdmin):
    pass


class OcultarModeloAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
