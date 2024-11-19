from django.contrib import admin
from .models import Evento, Feriado, TipoEvento
# Register your models here.
admin.site.register(Evento)
admin.site.register(Feriado)
admin.site.register(TipoEvento)