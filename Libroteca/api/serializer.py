from rest_framework import serializers
from Sistema.models import Usuario

# serializer para usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            '__all__'
        )
        model=Usuario