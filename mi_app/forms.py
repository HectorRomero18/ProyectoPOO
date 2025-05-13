from django import forms
from .models import Cargo, Departamento, Empleado ,Rol

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'