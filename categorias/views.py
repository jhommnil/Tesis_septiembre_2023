from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Marca, Producto, Modelo, Tipo
from .forms import ProductoForm

# Create your views here.
def Listar (request):

    productos = Producto.objects.all()
    marcas = Marca.objects.all()
    modelos = Modelo.objects.all()
    tipos = Tipo.objects.all()
    contenido = {'productos': productos,
                 'marcas': marcas,
                 'modelos': modelos,
                 'tipos': tipos}
    return render(request,'LisCategoria.html',contenido)

def AgregarCategoria (request):
    formulario = ProductoForm(request.POST or None, request or None )
    if formulario.is_valid():
        formulario.save()
        return redirect('ListarCT')
    return render(request,'AgregarCategoria.html', {'formulario': formulario} )

def EditarCategoria(request, N_producto):
    productos=Producto.objects.get(N_producto=N_producto)
    formualrio=ProductoForm(request.POST or None, request.FILES or None, instance=productos)
    if formualrio.is_valid() and request.method =='POST':
        formualrio.save()
        return redirect('ListarCT')
    return render(request,'EditarCategoria.html', {'formulario': formualrio})

def EliminarCategoria(request, N_producto):
    productos=Producto.objects.get(N_producto=N_producto)
    productos.delete()
    return redirect('ListarCT')