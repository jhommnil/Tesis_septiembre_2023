from django import forms
from .models import Producto, Marca, Modelo, Tipo

class ProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        
class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'
        
class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'