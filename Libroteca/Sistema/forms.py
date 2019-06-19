from django import forms
from .models import Libro
from .models import Reserva
from django.utils import timezone

#clase que crea los campos y sus tipos para realizar el login
choices=(
    ('Nuevo', 'Nuevo'),
    ('Usado', 'Usado')
)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Password")

class AgregarLibro(forms.ModelForm):
    class Meta:
        model= Libro

        fields = [
            'nombreLibro',
            'descripcionLibro',
            'fotoLibro',
            'estadoLibro',
        ]

        labels = {
            'nombreLibro' : 'Nombre',
            'descripcionLibro' : 'Descripcion',
            'fotoLibro' : 'Foto',
            'estadoLibro' : 'Estado',
        }

        widgets = {
            'nombreLibro' : forms.TextInput(attrs={'class':'form'}),
            'descripcionLibro' : forms.TextInput(attrs={'class':'form'}),
            'estadoLibro' : forms.Select(choices=choices),
        }

class AgregarReserva(forms.ModelForm):
    class Meta:
        model= Reserva

        fields = [
            'idLibro',
            'nombreLibro',
            'estadoLibro',
        ]

        labels = {
            'idLibro' : 'ID',
            'nombreLibro' : 'Nombre',
            'estadoLibro' : 'Estado',
        }

        widgets = {
            'idLibro' : forms.TextInput(attrs={'class':'form', 'readonly' : 'true'}),
            'nombreLibro' : forms.TextInput(attrs={'class':'form', 'readonly' : 'true'}),
            'estadoLibro' : forms.TextInput(attrs={'class':'form', 'readonly' : 'true'}),
        }
   