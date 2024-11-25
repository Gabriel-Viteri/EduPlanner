from rest_framework import viewsets
from .serializers import EventoSerializer, TipoEventoSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from core.models import Evento, TipoEvento

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

class TipoEventoViewSet(viewsets.ModelViewSet):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Solo los usuarios autenticados pueden acceder

