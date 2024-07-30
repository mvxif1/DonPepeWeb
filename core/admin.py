from django.contrib import admin
from .models import Usuario, Rol, Region, Comuna, Venta, Categoria, Producto, DetalleVenta, TipoDespacho, Estado, Direccion
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetalleVenta)
admin.site.register(TipoDespacho)
admin.site.register(Estado)
admin.site.register(Direccion)