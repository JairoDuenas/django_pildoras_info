from django.http import HttpResponse
import datetime
from django.template import loader
from django.shortcuts import render

class Persona(object):
  def __init__(self, nombre, apellido):
    self.nombre=nombre
    self.apellido= apellido

def saludo(request): # Primera vista

  persona1=Persona("Profesor Juan", "Díaz")

  temas_del_curso=[
    "Plantillas",
    "Modelos",
    "Formularios",
    "Vistas",
    "Despliegue"
    ]

  ahora=datetime.datetime.now()

  context={
    "nombre_persona":persona1.nombre,
    "apellido_persona":persona1.apellido,
    "momento_actual":ahora,
    "temas":temas_del_curso
    }

  return render(request, "plantilla1.html", context)

def despedida(request):
  return HttpResponse("Hasta luego alumnos django")

def curso_c(request):
  fecha_actual=datetime.datetime.now()
  return render(request, "curso_c.html", {"dameFecha":fecha_actual})

def curso_css(request):
  fecha_actual=datetime.datetime.now()
  return render(request, "curso_css.html", {"dameFecha":fecha_actual})


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