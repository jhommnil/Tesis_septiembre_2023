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
    stock = models.CharField(default=0)
    fecha_registro = models.DateTimeField(auto_now_add=True)

