from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio/inicio.html')

def servicios(request):
    return render(request, 'inicio/index.html')

def sobreNosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')

def MiCuenta(request):
    return render(request, 'inicio/mi_cuenta.html')