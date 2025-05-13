from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Cargo, Departamento, Empleado
from .forms import CargoForm, DepartamentoForm, EmpleadoForm


def home(request):
    data = {
        'title': 'Sistema de Nómina de Pagos',
        'description': 'Gestión de nóminas',
        'author': 'The Fantastic Four',
        'year': 2025,
    }
    # doctores = Doctor.objects.all()
    # data["doctores"]=doctores
    #return HttpResponse("<h1>Hello,Mi primer pagina con django</h1>")
    #return JsonResponse(data)  
    return render(request, 'home.html', data)




# Vistas para el CRUD del modelo Cargo
def create_cargo(request):
    
    if request.method == 'POST':
        form = CargoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:list_cargo')
    else:
        form = CargoForm()
    return render(request, 'Cargo/create_cargo.html', {'form': form})

def mostrar_cargos(request):
    query = request.GET.get('q')

    if query:
        cargos = Cargo.objects.filter(descripcion__icontains=query)
    else:
        cargos = Cargo.objects.all()
    return render(request, 'Cargo/list.html', {'cargos': cargos})

def delete_cargo(request, id):
    cargo = get_object_or_404(Cargo, id=id)
    cargo.delete()
    return redirect('core:list_cargo')

def update_cargo(request, id):
    cargo = get_object_or_404(Cargo, id=id)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('core:list_cargo')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'Cargo/update_cargo.html', {'form': form})


# Vistas para el CRUD del modelo Departamento
def create_departamento(request):
    
    if request.method == 'POST':
        form = DepartamentoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:list_departamento')
    else:
        form = DepartamentoForm()
    return render(request, 'Departamento/create_departamento.html', {'form': form})

def mostrar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'Departamento/list.html', {'departamentos': departamentos})

def delete_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    departamento.delete()
    return redirect('core:list_departamento')

def update_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            return redirect('core:list_departamento')
    else:
        form = DepartamentoForm(instance=departamento)
    return render(request, 'Departamento/update_departamento.html', {'form': form})


# ************************Vistas para el CRUD de Empleado*****************************************

def create_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:list_empleado')
    else:
        form  = EmpleadoForm()
    return render(request, 'Empleado/create_empleado.html', {'form': form})

def mostrar_empleado(request):
    query = request.GET.get('q')
    if query:
        empleado = Empleado.objects.filter(cedula__icontains=query)
    else:
        empleado = Empleado.objects.all()
    return render(request, 'Empleado/list.html', {'empleados': empleado})

def delete_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect('core:list_empleado') 

def update_empleado(request,id):
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        form.save()
        return redirect('core:list_empleado')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'Empleado/update_empleado.html', {'form': form})

# ************************Vistas para el CRUD de Rol*****************************************

def create_rol(request):
    pass

def mostrar_rol(request):
    pass

def delete_rol(request, id):
    pass

def update_rol(request,id):
    pass