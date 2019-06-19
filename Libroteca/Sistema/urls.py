from django.conf.urls import url, include
from . import views as vistas
from django.urls import path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^index/$', vistas.index, name="index"),
    url(r'^$', vistas.index, name="inicio"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),#permite la inclusion de las vistas de login de github
    path(r'base_layout',vistas.base_layout,name='base_layout'),#permite inclusion de la vista para el serviceworker
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^gestionarUsuarios/$', vistas.gestionarUsuarios, name="gestionarUsuarios"),
    url(r'^gestionarLibro/$', vistas.gestionarLibro, name="gestionarLibro"),
    url(r'^ListaLibros/$',vistas.ListaLibros,name="ListaLibros"),
    url(r'^ListaLibros/añadir/(?P<pk>[0-9]+)/$', vistas.añadirReserva, name="añadirReserva"),
    url(r'^ListaLibros/eliminar/(?P<pk>[0-9]+)/$',vistas.eliminarReserva, name="eliminarReserva"),   
    url(r'^registro/$',vistas.registro,name="registro"),
    url(r'^login/$',vistas.ingresar,name="login"),
    url('^', include('django.contrib.auth.urls')),#permite la inclusion de las vistas predeterminadas de python para el cambio de contraseña
    url(r'^salir/$',vistas.salir,name="salir"), 
    url(r'^libro/delete/(?P<postid>\d+)/', vistas.delete_post, name="delete_post"),
    url(r'^modificarLibro/(?P<pk>[0-9]+)/$', vistas.modificarLibro, name="modificarLibro"),
    url(r'^verReserva', vistas.verReserva, name="verReserva"),
    url(r'^eliminarReserva/(?P<pk>[0-9]+)/$', vistas.eliminarReserva, name="eliminarReserva"),
         
]