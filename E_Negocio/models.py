from django.db import models
# Create your models here.
#Estructura de negocio

class TipoCanal(models.Model):
    id_recurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Tipos de Canales"

    def __str__(self):
        return self.nombre

class Canales(models.Model):
    id_canales  = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoCanal, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Canales"

    def __str__(self):
        return self.nombre

class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Participantes"

    def __str__(self):
        return self.nombre
    
class Actividades(models.Model):
    id_actividad  = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    canal = models.ForeignKey(Canales, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    id_recurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.nombre

class Componente(models.Model):
    id_componente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    canal = models.ForeignKey(Canales, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Componentes"

    def __str__(self):
        return self.nombre
