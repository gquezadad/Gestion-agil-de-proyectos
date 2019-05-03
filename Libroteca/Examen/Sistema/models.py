from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# clase que crea el modelo producto
class Producto(models.Model):
    nombreProducto=models.CharField(max_length=50 ,blank=False,null=False)
    costoPresupuestado=models.CharField(max_length=50, null=True)
    costoReal=models.CharField(max_length=300, null=True)
    tiendaProducto=models.CharField(max_length=100, null=True)
    notaAdicional=models.CharField(max_length=100, null=True)

# clase que crea el modelo usuario
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Agregamos datos
    perfil=models.CharField(max_length=20,default="Usuario")
    rut=models.CharField(max_length=15,primary_key=True)
    nombre=models.CharField(max_length=100,blank=False)

# clase que crea el modelo tienda
class Tienda(models.Model):
    nombreTienda=models.CharField(max_length=50 ,blank=False,null=False)
    nombreSucursal=models.CharField(max_length=50, null=True)
    direccion=models.CharField(max_length=300, null=True)
    region=models.CharField(max_length=300,null=True,default="Online")
    ciudad=models.CharField(max_length=100, null=True,default="Online")

# clase que crea el modelo lista
class Lista(models.Model):
    Productos=models.ManyToManyField(Producto) 
    usuario=models.ForeignKey(User, related_name='dueño', null=True, on_delete='CASCADE')
    nombreLista=models.CharField(max_length=50 ,blank=False,null=False)