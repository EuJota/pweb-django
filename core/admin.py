from django.contrib import admin
from .models import Grupo_veiculo, Usuario, Veiculo, Seguro, Reserva, Manutencao


admin.site.register(Usuario)
admin.site.register(Grupo_veiculo)
admin.site.register(Veiculo)
admin.site.register(Seguro)
admin.site.register(Reserva)
admin.site.register(Manutencao)


# Register your models here.
