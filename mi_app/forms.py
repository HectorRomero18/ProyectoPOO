from django import forms
from .models import Cargo, Departamento, Empleado ,Rol, TipoContrato, Prestamo

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
        fields = ['empleado', 'aniomes', 'sueldo', 'horas_extra', 'bono']
        labels = {
            'aniomes': 'Mes y Año de la Nómina',  # Nuevo nombre que se mostrará
        }
        widgets = {
            'aniomes': forms.DateInput(attrs={'type': 'date'}),
        }
    
class ContratoForm(forms.ModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'
        
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['empleado', 'tipo_prestamo', 'fecha_prestamo', 'monto','numero_cuotas']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
        }