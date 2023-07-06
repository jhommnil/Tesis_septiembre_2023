from django.db import models
from stock.models import StockTienda
from categorias.models import Modelo

class Venta(models.Model):
    stocktienda = models.ForeignKey(StockTienda, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Verificar si hay suficiente stock del producto antes de realizar la venta
        if self.cantidad > self.stocktienda.stock:
            raise ValueError("No hay suficiente stock del producto")

        # Actualizar el stock después de la venta
        self.stocktienda.stock -= self.cantidad
        self.stocktienda.save()

        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"Stock: {self.stocktienda} - Modelo: {self.modelo} - Cantidad: {self.cantidad} - Fecha: {self.fecha}"

