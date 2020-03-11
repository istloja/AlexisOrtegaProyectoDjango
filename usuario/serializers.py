from rest_framework import serializers
from .models import Usuario,Equipo

class UsuarioSerealizable(serializers.ModelSerializer):
    """docstring for UsuarioSerealizable."""

    class Meta:
        model = Usuario
        fields=(
            'nombre',
            'apellido',
        )

class EquipoSerealizable(serializers.ModelSerializer):
    """docstring for EquipoSerealizable."""

    class Meta:
        model = Equipo
        fields=(
            'nombre',
            'descripcion',
            'disponible'
        )
