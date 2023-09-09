from django.shortcuts import render
from django.shortcuts import redirect
from .models import Venta
from .forms import VentaForm
from django.contrib import messages

def ListarVentas(request):
    ventas = Venta.objects.all()
    contexto = {'ventas': ventas}
    return render(request, 'ListarVenta.html', contexto)

def AgregarVenta(request):
    if request.method == 'POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid():
            venta = formulario.save(commit=False)
            if not venta.save():
                messages.error(request, "No hay suficiente stock del producto para realizar la venta.")
                return redirect('AgregarVenta')  # Redireccionar a la misma página para mostrar el mensaje
            return redirect('ListarVenta')  # Redireccionar a la lista de ventas si la venta fue exitosa
    else:
        formulario = VentaForm()
    contexto = {
        'formulario': formulario,
    }
    return render(request, 'AgregarVenta.html', contexto)

def EditarVenta(request, id):
    venta=Venta.objects.get(id=id)
    formualrio=VentaForm(request.POST or None, request.FILES or None, instance=venta)
    if formualrio.is_valid() and request.method =='POST':
        formualrio.save()
        return redirect('ListarVenta')
    return render(request,'EditarVenta.html', {'formulario': formualrio})

def EliminarVenta(request, id):
    ventas=Venta.objects.get(id=id)
    ventas.delete()
    return redirect('ListarVenta')