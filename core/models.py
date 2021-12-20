from django.db import models


class Usuario(models.Model):
    role = models.CharField(max_length=20)
    nome = models.CharField(max_length=40)
    endereco = models.CharField(max_length=100)
    cpf = models.IntegerField(unique=True)
    rg = models.IntegerField(unique=True)
    cnh = models.IntegerField(unique=True)
    email = models.EmailField()
    senha = models.CharField(max_length=40)
    setor = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    administrador = models.BooleanField()
    cnpj = models.IntegerField(unique=True)
    aprovado = models.BooleanField()

    def __str__(self):
        return self.nome


class Grupo_veiculo(models.Model):
    tipo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tipo


class Veiculo(models.Model):
    tipo = models.ForeignKey(Grupo_veiculo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=20)
    placa = models.CharField(max_length=10, unique=True)
    cor = models.CharField(max_length=20)
    chassi = models.CharField(max_length=40)
    remavam = models.CharField(max_length=40)
    foto = models.CharField(max_length=500)
    gps = models.IntegerField()
    quilometragem = models.IntegerField()
    portas = models.IntegerField()
    assentos = models.IntegerField()
    nivelCombustivel = models.FloatField()
    disponibilidade = models.BooleanField()
    estado = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Seguro(models.Model):
    tipo = models.CharField(max_length=10, unique=True)
    empresa = models.CharField(max_length=70, default=0)

    def __str__(self):
        return self.tipo


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    tipoSeguro = models.ForeignKey(Seguro, on_delete=models.CASCADE)
    periodoInicial = models.DateField()
    periodoFinal = models.DateField()

    def __str__(self):
        return f'{self.usuario} - {self.veiculo}'


class Manutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)

    def __str__(self):
        return self.veiculo
