from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# clase que crea el modelo usuario
class Usuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #Agregamos datos
    perfil=models.CharField(max_length=20,default="Usuario")
    rut=models.CharField(max_length=15,primary_key=True)
    nombre=models.CharField(max_length=100,blank=False)

class Libro(models.Model):
    idLibro=models.AutoField(primary_key=True, null=False)
    nombreLibro=models.CharField(max_length=50 ,blank=False,null=False)
    descripcionLibro=models.CharField(max_length=300)
    fotoLibro=models.ImageField(upload_to='./media/',default='./media/noname.jpg')
    estadoLibro=models.CharField(max_length=100, default="Seleccione", null=True)