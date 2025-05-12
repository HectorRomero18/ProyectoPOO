from django import forms
from .models import Cargo, Departamento

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'