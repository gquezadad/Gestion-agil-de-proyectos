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
    url(r'^gestionarProducto/$', vistas.gestionarProducto, name="gestionarProducto"),
    url(r'^gestionarListas/$', vistas.gestionarListas, name="gestionarProducto"),
    url(r'^gestionarTiendas/$', vistas.gestionarTiendas, name="gestionarTiendas"),
    url(r'^registro/$',vistas.registro,name="registro"),
    url(r'^login/$',vistas.ingresar,name="login"),
    url('^', include('django.contrib.auth.urls')),#permite la inclusion de las vistas predeterminadas de python para el cambio de contraseña
    url(r'^salir/$',vistas.salir,name="salir"),
    
]