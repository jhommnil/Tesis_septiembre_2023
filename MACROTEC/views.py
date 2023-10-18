from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def Inicio(request):
    return render(request,'Inicio.html')

def Index(request):
    return render(request,'index.html')