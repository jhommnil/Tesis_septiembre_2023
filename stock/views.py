from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import StockTienda
from .forms import StockTiendaForm
# Create your views here.

#definiciondes del listar
def ListarStock (request):
    stocktienda = StockTienda.objects.all()
    contenido = {'stocktienda':stocktienda}
    return render(request,'ListarStock.html',contenido)

#definiciones del agregar
def AgregarStockTienda(request):
    if request.method == 'POST':
        formulario = StockTiendaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('ListarSTOCK') 
    else:
        formulario = StockTiendaForm()

    contexto = {
        'formulario': formulario,
    }
    
    return render(request, 'AgregarStock.html', contexto)

#definiciones del editar
def EditarStockTienda(request, id):
    stocktienda=StockTienda.objects.get(id=id)
    formualrio=StockTiendaForm(request.POST or None, request.FILES or None, instance=stocktienda)
    if formualrio.is_valid() and request.method =='POST':
        formualrio.save()
        return redirect('ListarSTOCK')
    return render(request,'EditarStock.html', {'formulario': formualrio})

#definiciones de eliminar
def EliminarStockTienda(request, id):
    stoktienda=StockTienda.objects.get(id=id)
    stoktienda.delete()
    return redirect('ListarSTOCK')