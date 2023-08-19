from django import forms
from .models import Producto, Marca, Modelo, Tipo

class ProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'