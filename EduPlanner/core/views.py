from django.shortcuts import render,redirect
from .models import Feriado , Evento
from creds import api_key
from django.contrib.auth import login
from django.contrib import messages
from .forms import FormularioInicioSesion,FormularioRegistro, FormularioEvento
from django.contrib.auth import authenticate
import requests
from django.contrib.auth.decorators import login_required
# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
@api_view(['POST'])
@permission_classes([IsAdminUser])
def get_auth_token(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

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
@login_required
def eventos(request):
    titulo = "Eventos"
    if request.method == 'POST':
        form = FormularioEvento(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento creado exitosamente")
            return redirect('eventos')
    else:
        token, created = Token.objects.get_or_create(user=request.user)
        form = FormularioEvento(initial={'auth_token': token.key})
    data = {
        "titulo": titulo,
        "form": form
    }
    return render(request, 'core/eventos.html', data)
def registrarse(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = FormularioRegistro()
    return render(request, 'core/registrarse.html', {'form': form})
def iniciarSesion(request):
    if request.method == 'POST':
        form = FormularioInicioSesion(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Correo o contraseña incorrectos")
    else:
        form = FormularioInicioSesion()
    return render(request, 'core/inicioSesion.html', {'form': form})