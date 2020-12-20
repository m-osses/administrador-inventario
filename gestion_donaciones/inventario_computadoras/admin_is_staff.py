from django.contrib.admin import AdminSite, ModelAdmin
from .models import Computadora, Microprocesador, TarjetaMemoriaRam, DiscoRigido, SistemaOperativo


class StaffAdminSite(AdminSite):
    def has_permission(self, request):
        if not super().has_permission(request):
            return False
        return request.user.is_staff


admin_staff = StaffAdminSite(name="admin-colaboradores")

admin_staff.site_header = "Panel Colaboradores ATSV"


class ColaboradorBaseModelAdmin(ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


class OcultarModeloAdmin(ColaboradorBaseModelAdmin):
    def get_model_perms(self, request):
        return {}


class ComputadoraAdmin(ColaboradorBaseModelAdmin):
    list_display = ('id', 'formato', 'procesador', 'memoria', 'disco', 'sist_op', 'cambio_pasta', 'estado', 'notas')
    list_filter = ('estado',)


class MicroprocesadorAdmin(OcultarModeloAdmin):
    pass


class TarjetaMemoriaRamAdmin(OcultarModeloAdmin):
    pass


class DiscoRigidoAdmin(OcultarModeloAdmin):
    pass


class SistemaOperativoAdmin(OcultarModeloAdmin):
    pass


admin_staff.register(Computadora, ComputadoraAdmin)
admin_staff.register(Microprocesador, MicroprocesadorAdmin)
admin_staff.register(TarjetaMemoriaRam, TarjetaMemoriaRamAdmin)
admin_staff.register(DiscoRigido, DiscoRigidoAdmin)
admin_staff.register(SistemaOperativo, SistemaOperativoAdmin)
