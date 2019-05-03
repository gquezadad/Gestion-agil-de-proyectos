from django.contrib import admin
from .models import Usuario,Producto,Tienda,Lista

# Register your models here.
# Crea el espacio para los objetos
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Tienda)
admin.site.register(Lista)