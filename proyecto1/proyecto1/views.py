from django.http import HttpResponse

def saludo(request): # Primera vista
  return HttpResponse("Hola alumnos, esta es la primera página con django")

def despedida(request):
  return HttpResponse("Hasta luego alumnos django")