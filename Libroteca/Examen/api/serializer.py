from rest_framework import serializers
from Sistema.models import Producto,Usuario,Tienda,Lista

# serializer para Producto
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Producto

# serializer para usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Usuario

# serializer para Tienda
class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Tienda

# serializer para Lista
class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Lista