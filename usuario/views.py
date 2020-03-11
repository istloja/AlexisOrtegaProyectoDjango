from django.shortcuts import render,redirect
from rest_framework import viewsets
from .serializers import UsuarioSerealizable, EquipoSerealizable
from .models import Usuario, Equipo
# Create your views here.

class UsuarioVista(viewsets.ModelViewSet):
    """docstring for UsuarioVista."""
    serializer_class = UsuarioSerealizable
    queryset = Usuario.objects.all()

class EquipoVista(viewsets.ModelViewSet):
    """docstring for UsuarioVista."""
    serializer_class = EquipoSerealizable
    queryset = Equipo.objects.all()
