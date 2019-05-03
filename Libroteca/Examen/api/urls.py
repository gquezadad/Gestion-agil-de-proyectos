from django.conf.urls import url, include
from . import views as vistas

# Urls utilizadas para obtnere información de los objetos
urlpatterns = [
    url(r'^serializerUsuarios/$', vistas.UsuariosLista.as_view(), name='serializerUsuario'),
    url(r'^serializerProductos/$', vistas.ProductosLista.as_view(), name='serializerProductos'),#url para la lista de usuarios con serializer
    url(r'^serializerTiendas/$', vistas.TiendasLista.as_view(), name='serializerTiendas'),#url para la lista de usuarios con serializer
    url(r'^serializerListas/$', vistas.ListasLista.as_view(), name='serializerListas'),#url para la lista de usuarios con serializer
    url(r'^mascota/delete/(?P<postid>\d+)/', vistas.delete_post, name="delete_post"),

]