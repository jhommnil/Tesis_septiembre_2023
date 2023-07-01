from django.db import models
from stock.models import StockTienda
class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Verificar si hay suficiente stock del producto antes de realizar la venta
        if self.cantidad > self.producto.stock:
            raise ValueError("No hay suficiente stock del producto")

        # Actualizar el stock después de la venta
        self.producto.stock -= self.cantidad
        self.producto.save()

        super(Venta, self).save(*args, **kwargs)

    def __str__(self):
        return f"Producto: {self.producto} - Marca: {self.marca} - Modelo: {self.modelo} - Cantidad: {self.cantidad} - Fecha: {self.fecha}"
