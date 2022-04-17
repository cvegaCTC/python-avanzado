from django.db import models


class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    fechaNacimiento = models.DateField()


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    fechaNacimento = models.DateField()
    especie = models.CharField(max_length=100)

    class Sexo(models.TextChoices):
        MACHO = 'Macho',
        HEMBRA = 'Hembra'

    sexo = models.CharField(max_length=6, choices=Sexo.choices)

    tutor = models.ForeignKey('Usuario', on_delete=models.CASCADE,)
