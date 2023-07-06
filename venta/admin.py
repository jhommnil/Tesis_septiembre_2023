from django.contrib import admin
from venta.models import Venta
# Register your models here.

#se impleta un clase para mostrar en el administrador de django
class VentasAdmin(admin.ModelAdmin):
    list_display = ('stocktienda','modelo','cantidad','fecha',)
admin.site.register(Venta,VentasAdmin)