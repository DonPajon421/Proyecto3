from rest_framework import serializers

from .models import Mascota, Responsable


class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ['id', 'nombre', 'correo', 'rut']


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'anio_nacimiento', 'especie', 'responsable']
