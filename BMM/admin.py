from django.contrib import admin
from .models import Mision, Politica, Regla, Estrategia, Meta, Objetivo, Tacticas, Vision

# Register your models here.
admin.site.register((Mision, Politica, Regla, Estrategia, Meta, Objetivo, Tacticas, Vision))

