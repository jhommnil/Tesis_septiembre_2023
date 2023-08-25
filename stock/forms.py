from django import forms
from .models import StockTienda
from categorias.models import Producto, Marca, Modelo, Tipo

class StockTiendaForm(forms.ModelForm):
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), label='Producto')
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), label='Marca')
    modelo = forms.ModelChoiceField(queryset=Modelo.objects.all(), label='Modelo')
    tipo = forms.ModelChoiceField(queryset=Tipo.objects.all(), label='Tipo')

    class Meta:
        model = StockTienda
        fields = '__all__'