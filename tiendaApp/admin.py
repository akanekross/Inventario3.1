from django.contrib import admin
from tiendaApp.models import Venta
from tiendaApp.models import Boleta
from tiendaApp.models import Usuario

# Register your models here.
class VentaAdmin(admin.ModelAdmin):
    list_display=['id', 'Cventa', 'Cproductos', 'Descripcion', 'Cantidad', 'Categoria','PrecioT']

class BoletaAdmin(admin.ModelAdmin):
    list_display=['id','Nboleta','Rutl','DiLocal','fecha','telefono','NomLocal']

class UsuarioAdmin(admin.ModelAdmin):
    list_display=['id','nombre','apellido','cargo','email','fono','direccion']



admin.site.register(Venta,VentaAdmin)
admin.site.register(Boleta,BoletaAdmin)
admin.site.register(Usuario,UsuarioAdmin)