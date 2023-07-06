from django.db import models
from categorias.models import Producto, Marca, Modelo, Tipo
# Create your models here.

# esta calse se esta creando para ver el stock de la tienda

class StockTienda(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    precio_compra = models.DecimalField(max_digits=8, decimal_places=2)
    Precio_venta = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField( default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.producto} - {self.marca}"

class IngresoSuministro(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Actualizar el stock de la tienda al registrar un ingreso de suministro
        stock_tienda, created = StockTienda.objects.get_or_create(
            producto=self.producto,
            marca=self.marca,
            modelo=self.modelo,
        )
        stock_tienda.stock += self.cantidad
        stock_tienda.save()

        super(IngresoSuministro, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto} - {self.marca} - {self.modelo} - Cantidad: {self.cantidad}"