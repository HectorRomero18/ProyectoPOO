from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Cargo(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Departamento(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class TipoContrato(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento,
                                    on_delete=models.CASCADE)
    tipo_contrato = models.ForeignKey(TipoContrato,
                                    on_delete=models.CASCADE)

    @staticmethod
    def validar_cedula_ecuatoriana(cedula):
        if not cedula.isdigit():
            raise ValidationError("La cédula debe contener solo números.")

        if len(cedula) != 10:
            raise ValidationError("La cédula debe tener 10 dígitos.")

        provincia = int(cedula[0:2])
        if provincia < 1 or provincia > 24:
            raise ValidationError("El código de provincia es inválido.")

        tercer_digito = int(cedula[2])
        if tercer_digito >= 6:
            raise ValidationError("El tercer dígito es inválido para una cédula ecuatoriana.")

        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        suma = 0
        for i in range(9):
            valor = int(cedula[i]) * coeficientes[i]
            if valor >= 10:
                valor -= 9
            suma += valor

        digito_verificador = (10 - (suma % 10)) % 10

        if digito_verificador != int(cedula[9]):
            raise ValidationError("La cédula ingresada no es válida.")

class Rol(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    aniomes = models.DateField()#202501
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2)
    bono = models.DecimalField(max_digits=10, decimal_places=2)
    iess = models.DecimalField(max_digits=10, decimal_places=2)


    tot_ing = models.DecimalField(max_digits=10, decimal_places=2)
    tot_des = models.DecimalField(max_digits=10, decimal_places=2)
    neto = models.DecimalField(max_digits=10, decimal_places=2)