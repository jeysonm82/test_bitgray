from django.contrib import admin
from models import Clientes, Productos, Sedes, Compras, Log

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Sedes)
admin.site.register(Log)

class ComprasAdmin(admin.ModelAdmin):
    model = Compras
    list_display=('cliente', 'producto', 'sede', 'precio', 'descripcion', 'fecha')

admin.site.register(Compras, ComprasAdmin)
