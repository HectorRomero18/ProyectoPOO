from django.contrib import admin
from .models import Cargo, Departamento, Empleado, Rol, TipoContrato, TipoPrestamo,Prestamo

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(TipoContrato)
admin.site.register(TipoPrestamo)
admin.site.register(Prestamo)
