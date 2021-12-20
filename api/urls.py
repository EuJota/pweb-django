
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import *

router = routers.DefaultRouter()

router.register('usuarios', UsuarioViewSet)
router.register('grupoVeiculos', Grupo_veiculoViewSet)
router.register('veiculos', VeiculoViewSet)
router.register('seguros', SeguroViewSet)
router.register('reservas', ReservaViewSet)
router.register('manutencao', ManutencaoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
