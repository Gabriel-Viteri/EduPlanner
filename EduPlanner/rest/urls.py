from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet,TipoEventoViewSet,Feriados_fusionadosViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'tipos_evento',TipoEventoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/fusion/', Feriados_fusionadosViewSet.as_view(), name='feriados'),  # Nueva ruta para los feriados
]

