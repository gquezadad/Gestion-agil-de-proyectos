from django.conf.urls import url, include
from . import views as vistas

# Urls utilizadas para obtnere información de los objetos
urlpatterns = [
    url(r'^serializerUsuarios/$', vistas.UsuariosLista.as_view(), name='serializerUsuario') 
]