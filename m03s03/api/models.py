from django.db import models
from django.utils.translation import gettext_lazy as _


class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    fechaNacimiento = models.DateField()


class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    fechaNacimiento = models.DateField()
    especie = models.CharField(max_length=30, default='No especificado')

    class Sexo(models.TextChoices):
        HEMBRA = "hembra", _("Hembra")
        MACHO = "macho", _("Macho")

    sexo = models.CharField(max_length=6, choices=Sexo.choices)
    tutor = models.ForeignKey(to=Persona, on_delete=models.CASCADE)
