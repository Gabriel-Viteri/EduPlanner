from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from core.models import Evento, TipoEvento
from .serializers import EventoSerializer, TipoEventoSerializer
from rest_framework.views import APIView

# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAdminUser]
class TipoEventoViewSet(viewsets.ModelViewSet):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer
    permission_classes = [IsAdminUser]
