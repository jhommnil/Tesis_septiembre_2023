from django.db import models
from stock.models import StockTienda
from categorias.models import Producto, Marca
from django.contrib import messages


class Venta(models.Model):
    stocktienda = models.ForeignKey(Producto, on_delete=models.CASCADE)
    marca_producto = models.ForeignKey(Marca, on_delete=models.CASCADE, default=1 )
    modelo = models.ForeignKey(StockTienda, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            # Verificar si hay suficiente stock del producto antes de realizar la venta
            if self.cantidad > self.modelo.stock:
                raise ValueError("No hay suficiente stock del producto")

            # Actualizar el stock después de la venta
            self.modelo.stock -= self.cantidad
            self.modelo.save()

            super(Venta, self).save(*args, **kwargs)
        except ValueError as e:
            # Capturamos la excepción y mostramos un mensaje en el administrador
            messages.error(None, f"Error al realizar la venta: {e}")
    def _str_(self):
        return f"Stock: {self.stocktienda} - Marca: {self.marca_producto} - Modelo: {self.modelo} - Cantidad: {self.cantidad} - Fecha: {self.fecha}"