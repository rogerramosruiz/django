from django.db import models

# Create your models here.
class Corredor(models.Model):
    codigo = models.CharField(max_length=10)
    nombreCompleto = models.CharField(max_length=150)
    comision = models.DecimalField(max_digits = 16, decimal_places=2)
    codigoAPS = models.CharField(max_length=4)
    isActive = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.codigo} {self.nombreCompleto} {self.comision}'
