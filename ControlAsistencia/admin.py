from django.contrib import admin
from .models import Empleados, asistencias

# Register your models here.

admin.site.register(Empleados)
admin.site.register(asistencias)