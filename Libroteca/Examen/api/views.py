from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from Sistema.models import Usuario,Producto,Tienda,Lista
from . import serializer
# Create your views here.

# view para listar y registrar a los usuario
class UsuariosLista(APIView):
    def get(self,request):
        usuario = Usuario.objects.all()
        serializers = serializer.UsuarioSerializer(usuario,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        nombreusuario=request.POST.get('nombreusuario')
        email=request.POST.get('email')
        contrasenia=request.POST.get('contrasenia')
        usuario=User.objects.create_user(username=nombreusuario,password=contrasenia,email=email)
        rut=request.POST.get('rut')
        nombre=request.POST.get('nombre')
        perfil=request.POST.get('perfil')
        if perfil== "Administrador":
            usuario.is_staff = True
        else:
            usuario.is_staff = False
        usuario.save()
        af=Usuario(user=usuario,perfil=perfil,rut=rut,nombre=nombre)
        af.save()
        return Response()

# view para listar y registrar a los productos
class ProductosLista(APIView):
    def get(self,request):
        producto = Producto.objects.all()
        serializers = serializer.ProductoSerializer(producto,many=True)
        return Response(serializers.data)

    def post(self,request):
        nombreProducto=request.POST.get('nombreProducto')
        costoPresupuestado=request.POST.get('costoPresupuestado')
        costoReal=request.POST.get('costoReal')
        tiendaProducto=request.POST.get('tiendaProducto')
        notaAdicional=request.POST.get('notaAdicional')
        af=Producto(nombreProducto=nombreProducto,costoPresupuestado=costoPresupuestado,costoReal=costoReal,tiendaProducto=tiendaProducto, notaAdicional=notaAdicional)
        af.save()
        return Response()

# view para borrar productos    
def delete_post(request, postid):
        instance = get_object_or_404(Producto, id=postid)
        instance.delete()
        messages.add_message(request, messages.SUCCESS, "The post with id %s has been deleted! " %postid)
        return HttpResponseRedirect("/")    

# view para listar y registrar a tiendas
class TiendasLista(APIView):
    def get(self,request):
        tienda = Tienda.objects.all()
        serializers = serializer.TiendaSerializer(tienda,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        nombreTienda=request.POST.get('nombreTienda')
        nombreSucursal=request.POST.get('nombreSucursal')
        direccion=request.POST.get('direccion')
        region=request.POST.get('region')
        ciudad=request.POST.get('ciudad')
        af=Tienda(nombreTienda=nombreTienda,nombreSucursal=nombreSucursal,direccion=direccion,region=region,ciudad=ciudad)
        af.save()
        return Response()
    
# view para listar listas
class ListasLista(APIView):
    def get(self,request):
        lista =Lista.objects.all()
        serializers = serializer.ListaSerializer(lista,many=True)
        return Response(serializers.data)