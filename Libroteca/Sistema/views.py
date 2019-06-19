from django.shortcuts import render, render_to_response, redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Usuario, Libro, Reserva
from .forms import LoginForm, AgregarLibro, AgregarReserva 
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

@login_required(login_url='login')#determina que para ingresar al gestionar libros este debe primero estar logeado
#metodo que permite añadir a un libro
def gestionarLibro(request):
    libros=Libro.objects.all()
    form=AgregarLibro(request.POST or None, request.FILES or None)
    if form.is_valid():
        datos=form.cleaned_data
        regDB=Libro(idLibro=datos.get("idLibro"),
        nombreLibro=datos.get("nombreLibro"),
        descripcionLibro=datos.get("descripcionLibro"),
        estadoLibro=datos.get("estadoLibro"),
        fotoLibro=datos.get("fotoLibro"))
        regDB.save()
    form=AgregarLibro()
    titulo="Gestion de Libros"
    return render(request,"gestionarLibro.html",{'libros':libros,'form':form,'titulo':titulo,})

def modificarLibro(request, pk):
    libro=Libro.objects.get(idLibro=pk)
    if request.method == "GET":
        form = AgregarLibro
    else:
        form = AgregarLibro(request.POST or None,request.FILES or None,instance=libro)
        if form.is_valid():
            form.save()
        return redirect('gestionarLibro')
    return render(request, 'modificarLibro.html', {'form':form})

def ListaLibros(request):
    libros=Libro.objects.all()
    return render(request,"ListaLibros.html",{'libros':libros,})

#metodo utilizado para borrar un libro
def delete_post(request, postid):
    instance = get_object_or_404(Libro, idLibro=postid)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "The post with id %s has been deleted! " %postid)
    return HttpResponseRedirect("/gestionarLibro/")

#view para obtener el template para el serviceworker
def base_layout(request):
	template='maqueta.html'
	return render(request,template)    

@login_required
def añadirReserva(request,pk):
    libro=Libro.objects.get(idLibro=pk)
    reserva=Reserva.objects.all()
    if request.method == "GET":
        form = AgregarReserva(instance=libro)
    else:
        form = AgregarReserva(request.POST or None,request.FILES or None,instance=libro)
        if form.is_valid():
            datos=form.cleaned_data
            regDb=Reserva(
                idLibro=datos.get("idLibro"),
                nombreLibro=datos.get("nombreLibro"),
                estadoLibro=datos.get("estadoLibro"),
                usuario=request.user.username)
            regDb.save()
            form.save()
        return redirect('ListaLibros')
    return render(request, 'añadirReserva.html', {'form':form,'libro':libro})

def verReserva(request):
    reserva=Reserva.objects.all()
    return render(request,"verReserva.html",{'reserva':reserva,})

def eliminarReserva(request, pk):
    reserva=Reserva.objects.get(codigoReserva=pk)
    if request.method == "POST":
        reserva.delete()
        return redirect('verReserva')
    return render (request, 'eliminarReserva.html', {'reserva':reserva})