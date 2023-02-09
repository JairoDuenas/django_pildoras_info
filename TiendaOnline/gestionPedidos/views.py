from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
  return render(request, "busqueda_productos.html", {})

def buscar(request):
  if request.GET['prod']:
    #mensaje=f"Artículo buscado: {request.GET['prod']}"
    producto=request.GET['prod']
    articulos=Articulos.objects.filter(nombre__icontains=producto)
    return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
  else:
    mensaje="No has ingresado nada"
  return HttpResponse(mensaje)