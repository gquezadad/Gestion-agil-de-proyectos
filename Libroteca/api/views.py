from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from Sistema.models import Usuario
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