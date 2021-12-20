from rest_framework import serializers
from .models import Usuario, Grupo_veiculo, Usuario, Veiculo, Seguro, Reserva, Manutencao


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['role', 'id', 'nome', 'endereco', 'cpf', 'rg', 'cnh',
                  'email', 'senha', 'setor', 'cargo', 'administrador', 'cnpj']


class Grupo_veiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo_veiculo
        fields = ['id', 'tipo']


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'tipo', 'placa', 'cor', 'chassi', 'remavam', 'foto', 'gps',
                  'quilometragem', 'portas', 'assentos', 'nivelCombustivel', 'disponibilidade', 'estado']


class SeguroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguro
        fields = ['id', 'tipo', 'empresa']


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'usuario', 'veiculo',
                  'tipoSeguro', 'periodoInicial', 'periodoFinal']


class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = ['id', 'veiculo']
