from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet,TipoEventoViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'tipos_evento',TipoEventoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
