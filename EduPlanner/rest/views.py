import requests
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import EventoSerializer, TipoEventoSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from core.models import Evento, TipoEvento
from rest_framework.views import APIView
import requests
from creds import api_key



class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  


class TipoEventoViewSet(viewsets.ModelViewSet):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Solo los usuarios autenticados pueden acceder

class Feriados_fusionadosViewSet(APIView):
    def get(self, request, *args, **kwargs):
        # Obtener los feriados de la API externa (Calendarific)
        url = f"https://calendarific.com/api/v2/holidays?&api_key={api_key}&country=CL&year=2024"
        response = requests.get(url)
        feriados = response.json()
        print(feriados)

        # Procesar los feriados
        lista_feriados = []
        for p in feriados["response"]["holidays"]:
            feriado = {
                "name": p["name"],
                "description": p["description"],
                "country": p["country"]["name"],
                "date": p["date"]["iso"],
                "type": p["type"],
                "primary_type": p["primary_type"],
                "canonical_url": p["canonical_url"],
                "urlid": p["urlid"],
                "locations": p["locations"],
                "states": p["states"],
            }
            lista_feriados.append(feriado)

        # Obtener los eventos de la base de datos
        eventos = Evento.objects.all()

        # Fusionar los eventos y los feriados
        lista_eventos = []
        for evento in eventos:
            evento_data = {
                "name": evento.titulo,
                "description": evento.descripcion,
                "date": evento.fecha_inicio.isoformat(),  # Usar 'fecha_inicio' para la fecha
                "type": evento.tipo.tipo if evento.tipo else "No definido",  # Aquí usamos 'evento.tipo.tipo'
                "event_type": "evento",  # Marcamos como evento
            }
            lista_eventos.append(evento_data)

        # Fusionar eventos y feriados
        fusionados = lista_feriados + lista_eventos

        # Devolver la lista fusionada como respuesta
        data = {
            "fusion": fusionados,
        }

        return Response(data)

