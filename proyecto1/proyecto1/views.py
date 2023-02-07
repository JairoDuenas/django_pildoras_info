from django.http import HttpResponse
import datetime

def saludo(request): # Primera vista
  return HttpResponse("Hola alumnos, esta es la primera página con django")

def despedida(request):
  return HttpResponse("Hasta luego alumnos django")

# --------- Contenido dinámico ---------------------

def dameFecha(request):
  fecha_actual=datetime.datetime.now()

  fecha="""
  <body>
  <h2>
  Fecha y hora actual %s
  <h2>
  <body>
  """ % fecha_actual
  return HttpResponse(fecha)

def calculaEdad(request, edad, agno):

  periodo=agno-2023
  edad_futura=edad+periodo

  documento=f"""
  <html>
  <body>
  <h2>
  En el año {agno} tendrás {edad_futura} años
  <h2>
  <body>
  <html>
  """
  return HttpResponse(documento)