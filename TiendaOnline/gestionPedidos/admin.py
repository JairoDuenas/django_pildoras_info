from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class Clientes_admin(admin.ModelAdmin):
  list_display=("nombre", "direccion", "telefono")
  search_fields=("nombre", "telefono")

class Articulos_admin(admin.ModelAdmin):
  list_filter=("seccion",)

class Pedidos_admin(admin.ModelAdmin):
  list_display=("numero", "fecha", "entregado")
  list_filter=("fecha",)
  date_hierarchy="fecha"

admin.site.register(Clientes, Clientes_admin)
admin.site.register(Articulos, Articulos_admin)
admin.site.register(Pedidos, Pedidos_admin)
