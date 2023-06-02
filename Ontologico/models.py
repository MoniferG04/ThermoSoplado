from django.db import models

# Create your models here.
#Ontologico

class ThermoSoplado(models.Model):
    id_Thermo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "ThermoSoplado"

    def __str__(self):
        return self.nombre

class Maniqui(models.Model):
    id_maniqui = models.AutoField(primary_key=True)
    color = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=100)
    diseño = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Maniquies"

    def __str__(self):
        return self.genero

class Almacenamiento(models.Model):
    id_almacenamiento = models.AutoField(primary_key=True)
    Stock = models.CharField(max_length=100)
    capacidad = models.CharField(max_length=100)
    ubicacion = models.ForeignKey(ThermoSoplado, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Almacenamiento"

    def __str__(self):
        return self.capacidad

class Distribucion(models.Model):
    id_distribucion = models.AutoField(primary_key=True)
    direccionEntrega = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ubicacion = models.ForeignKey(ThermoSoplado, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Empaquetado y Distribucion"

    def __str__(self):
        return self.direccionEntrega

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    direcccion = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    id_Thermo = models.AutoField(primary_key=True)
    fecha = models.DateField()
    valor = models.CharField(max_length=100)
    distribucion = models.ForeignKey(Distribucion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    maniqui = models.ForeignKey(Maniqui, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.fecha
    
class Produccion(models.Model):
    id_produccion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    ubicacion = models.ForeignKey(ThermoSoplado, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Produccion"

    def __str__(self):
        return self.nombre

class Control(models.Model):
    id_control = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    fecha = models.DateField()
    produccion = models.ForeignKey(Produccion, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Control de calidad"

    def __str__(self):
        return str(self.id_control)


