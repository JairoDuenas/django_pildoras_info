from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): # Primera vista
  doc_externo=open("/Users/jhonjairoduenasvega/python/django_pildoras/proyecto1/proyecto1/plantillas/plantilla1.html")
  plantilla=Template(doc_externo.read())
  doc_externo.close()

  contexto=Context()

  documento=plantilla.render(contexto)

  return HttpResponse(documento)

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