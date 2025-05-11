from django.contrib import admin
from .models import Cargo, Departamento, Empleado, Rol, TipoContrato

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(Empleado)
admin.site.register(Rol)
admin.site.register(TipoContrato)
