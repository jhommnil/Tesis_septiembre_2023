from django.contrib import admin
from categorias.models import Producto, Marca, Modelo, Tipo
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = 'N_producto'
    admin.site.register(Producto, ProductoAdmin)


