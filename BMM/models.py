from django.db import models

# Create your models here.
#BMMM
class Mision(models.Model):
    id_mision  = models.AutoField(primary_key=True)
    descripcion = models.TextField()

    class Meta:
        verbose_name_plural = "Mision"

    def __str__(self):
        return self.descripcion

class Vision(models.Model):
    id_vision = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Vision"

    def __str__(self):
        return self.descripcion

class Objetivo(models.Model):
    id_objetivo = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    vision = models.ForeignKey(Vision, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Objetivos"
    def __str__(self):
        return self.descripcion

class Meta(models.Model):
    id_meta = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    objetivos = models.ForeignKey(Objetivo,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion

class Politica(models.Model):
    id_politica = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.descripcion
    

# Una estrategia puede tener varias tacticas y varias tacticas pueden tener una meta     
class Estrategia(models.Model):
    id_estrategia = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    mision = models.ForeignKey(Mision, on_delete=models.CASCADE)
    objectivo = models.ForeignKey(Objetivo, on_delete=models.CASCADE)
    politica = models.ForeignKey(Politica, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Estrategias"
    
    def __str__(self):
        return self.descripcion

class Regla(models.Model):
    id_regla = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    politica = models.ForeignKey(Politica, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class Tacticas(models.Model):
    id_tactica = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    meta = models.ForeignKey(Meta, on_delete = models.CASCADE)
    estrategia =models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    regla = models.ForeignKey(Regla, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Tacticas"

    def __str__(self):
        return self.descripcion
    