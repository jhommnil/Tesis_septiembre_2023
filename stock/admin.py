from django.contrib import admin
from stock.models import StockTienda, IngresoSuministro
# Register your models here.
#se crea una clase para mostrar en el gestor administrador de django
class StockTiendaAdmin (admin.ModelAdmin):
    list_display = ('producto','marca','modelo','tipo','precio_compra','Precio_venta','stock','fecha_registro',)
admin.site.register(StockTienda,StockTiendaAdmin)

class IngresoSuministroAdmin (admin.ModelAdmin):
    list_display = ('producto','marca','modelo','cantidad','fecha_registro',)
admin.site.register(IngresoSuministro,IngresoSuministroAdmin)


