from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Marca, Producto, Modelo, Tipo
from .forms import ProductoForm, MarcaForm, ModeloForm, TipoForm

#Geredando vistas y validando funciones del sistema 
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

def AgregarCategoriaMarca (request):
    formulario = MarcaForm(request.POST or None, request or None )
    if formulario.is_valid():
        formulario.save()
        return redirect('ListarCT')
    return render(request,'AgregarCategoriaMarca.html', {'formulario': formulario} )

def AgregarCategoriaModelo (request):
    formulario = ModeloForm(request.POST or None, request or None )
    if formulario.is_valid():
        formulario.save()
        return redirect('ListarCT')
    return render(request,'AgregarCategoriaModelo.html', {'formulario': formulario} )

def AgregarCategoriaTipo (request):
    formulario = TipoForm(request.POST or None, request or None )
    if formulario.is_valid():
        formulario.save()
        return redirect('ListarCT')
    return render(request,'AgregarCategoriaTipo.html', {'formulario': formulario} )

def EditarCategoria(request, N_producto):
    productos=Producto.objects.get(N_producto=N_producto)
    formualrio=ProductoForm(request.POST or None, request.FILES or None, instance=productos)
    if formualrio.is_valid() and request.method =='POST':
        formualrio.save()
        return redirect('ListarCT')
    return render(request,'EditarCategoria.html', {'formulario': formualrio})

def EditarCategoriaMarca(request, N_marca):
    marcas=Marca.objects.get(N_marca=N_marca)
    formualrio=MarcaForm(request.POST or None, request.FILES or None, instance=marcas)
    if formualrio.is_valid() and request.method =='POST':
        formualrio.save()
        return redirect('ListarCT')
    return render(request,'EditarCategoriaMarca.html', {'formulario': formualrio})

def EditarCategoriaModelo(request, N_modelo):
    modelos=Modelo.objects.get(N_modelo=N_modelo)
    formualrio=ModeloForm(request.POST or None, request.FILES or None, instance=modelos)
    if formualrio.is_valid() and request.method =='POST':
        formualrio.save()
        return redirect('ListarCT')
    return render(request,'EditarCategoriaModelo.html', {'formulario': formualrio})

def EditarCategoriaTipo(request, N_tipo):
    tipos=Tipo.objects.get(N_tipo=N_tipo)
    formualrio=TipoForm(request.POST or None, request.FILES or None, instance=tipos)
    if formualrio.is_valid() and request.method =='POST':
        formualrio.save()
        return redirect('ListarCT')
    return render(request,'EditarCategoriaTipo.html', {'formulario': formualrio})

def EliminarCategoria(request, N_producto):
    productos=Producto.objects.get(N_producto=N_producto)
    productos.delete()
    return redirect('ListarCT')

def EliminarCategoriaMarca(request, N_marca):
    marcas=Marca.objects.get(N_marca=N_marca)
    marcas.delete()
    return redirect('ListarCT')

def EliminarCategoriaModelo(request, N_modelo):
    modelos=Modelo.objects.get(N_modelo=N_modelo)
    modelos.delete()
    return redirect('ListarCT')

def EliminarCategoriaTipo(request, N_tipo):
    tipos=Tipo.objects.get(N_tipo=N_tipo)
    tipos.delete()
    return redirect('ListarCT')