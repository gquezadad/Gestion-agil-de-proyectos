from django import forms

#clase que crea los campos y sus tipos para realizar el login
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")