from rest_framework import routers
from .views import EventoViewSet,TipoEventoViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register('eventos', EventoViewSet)
router.register('tipo_evento', TipoEventoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]