from django.contrib import admin
from categorias.models import Producto, Marca, Modelo, Tipo

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('N_producto',)
admin.site.register(Producto, ProductoAdmin)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('N_marca',)
admin.site.register(Marca,MarcaAdmin)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('N_modelo',)
admin.site.register(Modelo,ModeloAdmin)

class TipoAdmin(admin.ModelAdmin):
    list_display = ('N_tipo',)
admin.site.register(Tipo,TipoAdmin)


