from django.db import models

# Create your models here.

class TipoEvento(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    descripcion_tipo = models.TextField()

    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name_plural = 'Tipos de Eventos'

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo = models.ForeignKey(TipoEvento, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos')

    def __str__(self):
        return self.titulo
    
    
class Feriado(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=2)
    date = models.DateField()
    type = models.CharField(max_length=100)
    primary_type = models.CharField(max_length=100)
    canonical_url = models.URLField()
    urlid = models.CharField(max_length=100)
    locations = models.CharField(max_length=100)
    states = models.CharField(max_length=100)

    def __str__(self):
        return self.name