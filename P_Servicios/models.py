from django.db import models
from Ontologico.models import ThermoSoplado
from E_Negocio.models import Canales
# Create your models here.
#Portafolio de servicios

class Negocios(models.Model):
    id_negocios  = models.AutoField(primary_key=True)
    nombre = models.TextField()
    canal = models.ForeignKey(Canales, on_delete=models.CASCADE)
    thermo = models.ForeignKey(ThermoSoplado, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Negocios"

    def __str__(self):
        return self.nombre

class Actores(models.Model):
    id_actor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    negocio = models.ForeignKey(Negocios, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Actores"

    def __str__(self):
        return self.nombre

class ObjetoNegocio(models.Model):
    id_linea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    Tipo = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Objeto de Negocio"

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    TipoServicip = models.CharField(max_length=100)
    actor = models.ForeignKey(Actores, on_delete=models.CASCADE)
    objeto = models.ForeignKey(ObjetoNegocio, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre

class LineaNegocio(models.Model):
    id_linea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    lineaNegocio = models.CharField(max_length=100)
    negocio = models.ForeignKey(Negocios, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Linea de negocio"

    def __str__(self):
        return self.nombre

