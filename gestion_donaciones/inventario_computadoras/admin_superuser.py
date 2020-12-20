from django.contrib.admin import AdminSite, ModelAdmin
from .models import Computadora, Microprocesador, TarjetaMemoriaRam, DiscoRigido, SistemaOperativo
from django.contrib.auth.models import User, Group


class SuperuserAdminSite(AdminSite):
    def has_permission(self, request):
        if not super().has_permission(request):
            return False
        return request.user.is_superuser


admin_su = SuperuserAdminSite(name="admin-superuser")

admin_su.site_header = "Panel Administración ATSV"


class ComputadoraAdmin(ModelAdmin):
    list_display = ('id', 'formato', 'procesador', 'memoria', 'disco', 'sist_op', 'cambio_pasta', 'estado', 'notas')
    list_filter = ('estado',)


class MicroprocesadorAdmin(ModelAdmin):
    pass


class TarjetaMemoriaRamAdmin(ModelAdmin):
    pass


class DiscoRigidoAdmin(ModelAdmin):
    pass


class SistemaOperativoAdmin(ModelAdmin):
    pass


admin_su.register(Computadora, ComputadoraAdmin)
admin_su.register(Microprocesador, MicroprocesadorAdmin)
admin_su.register(TarjetaMemoriaRam, TarjetaMemoriaRamAdmin)
admin_su.register(DiscoRigido, DiscoRigidoAdmin)
admin_su.register(SistemaOperativo, SistemaOperativoAdmin)
admin_su.register(User)
admin_su.register(Group)
