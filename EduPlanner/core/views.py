from django.shortcuts import render
from .models import Feriado , Evento
from creds import api_key
import requests


# Create your views here.

def home(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/index.html', data)

def feriados(request):
    titulo = "Feriados"
    info = requests.get("https://calendarific.com/api/v2/holidays?&api_key=" + api_key + "&country=CL&year=2024")
    feriados = info.json()
    
    lista_feriados = list()
    
    for p in feriados["response"]["holidays"]:
        feriado = Feriado(
            name = p["name"],
            description = p["description"],
            country = p["country"]["name"],
            date = p["date"]["iso"],
            type = p["type"],
            primary_type = p["primary_type"],
            canonical_url = p["canonical_url"],
            urlid = p["urlid"],
            locations = p["locations"],
            states = p["states"],            
        )
        
        lista_feriados.append(feriado)
    
    
    data = {
        "titulo":titulo,
        "feriados":lista_feriados,
    
    }
    return render(request,'core/feriados.html', data)

def eventos(request):
    titulo = "Eventos"
    data = {
        "titulo": titulo
    }
    return render(request,'core/eventos.html', data)
