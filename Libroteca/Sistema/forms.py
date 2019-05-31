from django import forms

#clase que crea los campos y sus tipos para realizar el login
choices=(
    ('Nuevo', 'Nuevo'),
    ('Usado', 'Usado')
)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Password")

class AgregarLibro(forms.Form):
    nombreLibro=forms.CharField(widget=forms.TextInput(), label="Nombre libro")
    descripcionLibro=forms.CharField(widget=forms.TextInput(), label="Descripción del Libro")
    fotoLibro=forms.ImageField(label="Foto del libro")
    estadoLibro=forms.ChoiceField( choices= choices, label="Estado del libro")