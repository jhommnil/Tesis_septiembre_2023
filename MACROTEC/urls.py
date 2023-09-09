"""MACROTEC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#se realiza las importaciones dependiendo a los necesitado
from django.contrib import admin
from django.urls import path
from categorias.views import Listar, AgregarCategoria,AgregarCategoriaMarca, AgregarCategoriaModelo,AgregarCategoriaTipo
from categorias.views import EditarCategoriaMarca, EditarCategoria, EditarCategoriaModelo, EditarCategoriaTipo
from categorias.views import EliminarCategoria,EliminarCategoriaMarca,EliminarCategoriaModelo,EliminarCategoriaTipo
from stock.views import ListarStock
from stock.views import AgregarStockTienda
from stock.views import EditarStockTienda
from stock.views import EliminarStockTienda
from .views import Inicio
from venta.views import ListarVentas, AgregarVenta, EditarVenta, EliminarVenta
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Inicio,name='Inicio'),
    #Update de los modulos
    path('ListarCT/', Listar,name='ListarCT'),
    path('ListarSTOCK/',ListarStock,name='ListarSTOCK'),
    path('ListarVenta/',ListarVentas,name='ListarVenta'),
    #Create de los modulos
    path('AgregarCTP/', AgregarCategoria, name='AgregarCTP'),
    path('AgregarCTM/', AgregarCategoriaMarca, name='AgregarCTM'),
    path('AgregarCTMD/',AgregarCategoriaModelo, name='AgregarCTMD'),
    path('AgregarCTT/',AgregarCategoriaTipo, name='AgregarCTT'), 
    path('AgregarSTOCK/',AgregarStockTienda,name='AgregarSTOCK'),
    path('AgregarVenta/',AgregarVenta,name='AgregarVenta'),
    #Update de los modulos
    path('EditarCT/<str:N_producto>', EditarCategoria, name='EditarCT'),
    path('EditarCTM/<str:N_marca>', EditarCategoriaMarca, name='EditarCTM'),
    path('EditarCTMD/<str:N_modelo>', EditarCategoriaModelo, name='EditarCTMD'),
    path('EditarCTT/<str:N_tipo>', EditarCategoriaTipo, name='EditarCTT'),  
    path('EditarSTOCK/<int:id>', EditarStockTienda, name='EditarSTOCK'),  
    path('EditarVenta/<int:id>', EditarVenta, name='EditarVenta'), 
    #Delete de los modulos
    path('EliminarCT/<str:N_producto>',EliminarCategoria, name='EliminarCT'),
    path('EliminarCTM/<str:N_marca>',EliminarCategoriaMarca, name='EliminarCTM'),
    path('EliminarCTMD/<str:N_modelo>',EliminarCategoriaModelo, name='EliminarCTMD'),
    path('EliminarCTT/<str:N_tipo>',EliminarCategoriaTipo, name='EliminarCTT'),
    path('EliminarSTOCK/<int:id>',EliminarStockTienda, name='EliminarSTOCK'),
    path('EliminarVenta/<int:id>',EliminarVenta, name='EliminarVenta'),
]

