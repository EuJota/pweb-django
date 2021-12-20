from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario, Grupo_veiculo, Veiculo, Seguro, Reserva, Manutencao
from .serializers import *


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class Grupo_veiculoViewSet(viewsets.ModelViewSet):
    queryset = Grupo_veiculo.objects.all()
    serializer_class = Grupo_veiculoSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class SeguroViewSet(viewsets.ModelViewSet):
    queryset = Seguro.objects.all()
    serializer_class = SeguroSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer
