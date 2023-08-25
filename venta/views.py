from django.shortcuts import render
from django.shortcuts import redirect
from .models import Venta
from .forms import VentaForms

def ListarVenta (request):
    venta = Venta.objects.all()
    contenido = {'venta':venta}
    return render(request,'ListarVenta.html',contenido)

def AgregarVenta(request):
    if request.method == 'POST':
        formulario = VentaForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('ListarSTOCK') 
    else:
        formulario = VentaForms()

    contexto = {
        'formulario': formulario,
    }
    
    return render(request, 'AgregarVenta.html', contexto)