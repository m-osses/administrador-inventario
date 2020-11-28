from django.db import models

class Microprocesador(models.Model):
    X64 = "X64"
    X86 = "X86"

    OPCIONES_ARQUITECTURA = [
        (X64, 'x64'),
        (X86, 'x86')
    ]

    nombre = models.CharField(max_length=50)
    arquitectura = models.CharField(
        max_length=3,
        choices=OPCIONES_ARQUITECTURA,
    )

class TarjetaMemoriaRam(models.Model):
    tamaño = models.IntegerField(max_length=5, help_text="En MB, ejemplo: 512, 1024, 2048")
    fabricante = models.CharField(max_length=10, blank=True)
    tipo = models.CharField(max_length=4, help_text="Ejemplo: DDR2, DDR3, etc.", blank=True)
    velocidad = models.CharField(max_length=10, blank=True)
     