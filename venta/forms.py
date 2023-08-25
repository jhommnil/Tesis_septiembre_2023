from django import forms
from .models import Venta
from categorias.models import Producto, Marca, Modelo

class VentaForms(forms.ModelForm):
    stocktienda = forms.ModelChoiceField(queryset=Producto.objects.all(), label='Producto')
    marca_producto = forms.ModelChoiceField(queryset=Marca.objects.all(), label='Marca')
    modelo = forms.ModelChoiceField(queryset=Modelo.objects.all(), label='Modelo')
    class Meta:
        model = Venta
        fields = '__all__'
    