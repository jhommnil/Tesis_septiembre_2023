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
        if self.cantidad > self.modelo.stock:
            self.error_message = "No hay suficiente stock del producto para realizar la venta."
            return False  # Indicate that the sale wasn't successful
        else:
            self.modelo.stock -= self.cantidad
            self.modelo.save()
            super(Venta, self).save(*args, **kwargs)
            return True  # Indicate that the sale was successful
    
    def __str__(self):
        return f"Stock: {self.stocktienda} - Marca: {self.marca_producto} - Modelo: {self.modelo} - Cantidad: {self.cantidad} - Fecha: {self.fecha}"
    
