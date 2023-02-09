from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import Formulario_contacto

# Create your views here.

def busqueda_productos(request):
  return render(request, "busqueda_productos.html", {})

def buscar(request):
  if request.GET['prod']:
    #mensaje=f"Artículo buscado: {request.GET['prod']}"
    producto=request.GET['prod']
    if len(producto)>20:
      mensaje="Texto demasiado largo, ingrese un texto válido"
    else:
      articulos=Articulos.objects.filter(nombre__icontains=producto)
      return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
  else:
    mensaje="No has ingresado nada"
  return HttpResponse(mensaje)

def contacto(request):
  if request.method=='POST':
    mi_formulario=Formulario_contacto(request.POST)
    if mi_formulario.is_valid():
      info_form=mi_formulario.cleaned_data

      send_mail(
        info_form['asunto'],
        info_form['mensaje'],
        info_form.get('email', ''), ['jairoduenas.ing@gmail.com'])
      return render(request, 'gracias.html')
  else:
    mi_formulario=Formulario_contacto()

  return render(request, 'formulario_contacto.html', {'form':mi_formulario})

  """ subject=request.POST["asunto"]
    message=request.POST["mensaje"] + " " + request.POST["email"]
    email_from=settings.EMAIL_HOST_USER
    recipient_list=["jairoduenas.ing@gmail.com"]
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'gracias.html')
  return render(request, 'contacto.html')"""