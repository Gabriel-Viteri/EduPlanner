from core.models import Evento,TipoEvento

from rest_framework import serializers

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'tipo']
class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = ["id","tipo","descripcion_tipo"]