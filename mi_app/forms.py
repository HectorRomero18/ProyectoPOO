from django import forms
from .models import Cargo, Departamento, Empleado ,Rol, TipoContrato

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

    def clean_cedula(self):
        cedula = self.cleaned_data['cedula']
        Empleado.validar_cedula_ecuatoriana(cedula)
        return cedula
    
        
class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'

class ContratoForm(forms.ModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'