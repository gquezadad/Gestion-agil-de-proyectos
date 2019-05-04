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
