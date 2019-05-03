from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Usuario,Tienda,Lista
from .forms import LoginForm 
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

# Create your views here.
# Vista inicio
def index(request):
    plantilla=loader.get_template("index.html")
    titulo="Libroteca"
    contexto={
        'titulo':titulo,
    }
    return HttpResponse(plantilla.render(contexto,request))

# Vista registro de usuario de tipo usuario 
def registro(request):
    return render(request,"registro.html",{'registro':registro,'titulo':"Registro",})

# Vista de registro de usuarios de administrador
@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    return render(request,"GestionarUsuario.html",{'actual':actual,'titulo':"Registro",})

# Vista para lista
@login_required(login_url='login')
def gestionarListas(request):
    lista=Lista.objects.all()
    return render(request,"GestionarLista.html",{'lista':lista,'titulo':"Gestion Listas",})

# Vista para productos
@login_required(login_url='login')
def gestionarProducto(request):
    producto=Producto.objects.all()
    titulo="Gestion de Productos"
    return render(request,"gestionarProducto.html",{'producto':producto,'titulo':titulo,})

# Vista para tiendas
@login_required(login_url='login')
def gestionarTiendas(request):
    tienda=Tienda.objects.all()
    titulo="Gestion de Tiendas"
    return render(request,"GestionarTienda.html",{'tienda':tienda,'titulo':titulo,})

#metodo utilizado para el ingreso ya registrado al sistema
def ingresar(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request, user)
            return redirect('index')
    titulo="Login"        
    return render(request,"login.html",{'form':form, 'titulo':titulo,})

# Redireccion al index cuando se realiza el logout
def salir(request) :
     logout(request)
     return redirect("/index/") 


#view para obtener el template para el serviceworker
def base_layout(request):
	template='maqueta.html'
	return render(request,template)
