from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Gasto(models.Model):
    usuario = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    monto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.categoria} ($ {self.monto})"
