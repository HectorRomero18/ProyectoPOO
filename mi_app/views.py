from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Cargo, Departamento, Empleado, TipoContrato , Rol
from .forms import CargoForm, DepartamentoForm, EmpleadoForm, ContratoForm , RolForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cargo, Departamento, Empleado, TipoContrato
from .forms import CargoForm, DepartamentoForm, EmpleadoForm, ContratoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    data = {
        'title': 'Sistema de Nómina de Pagos',
        'description': 'Gestión de nóminas',
        'author': 'The Fantastic Four',
        'year': 2025,
    }
    # doctores = Doctor.objects.all()
    # data["doctores"]=doctores
    # return HttpResponse("<h1>Hello,Mi primer pagina con django</h1>")
    # return JsonResponse(data)
    return render(request, 'home.html', data)


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('core:home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'USUARIO YA EXISTE!!!'
                })    
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'CONTRASEÑAS NO COINCIDEN!!!'})


def signout(request):
    logout(request)
    return redirect('core:signup')

def signin(request):
    if request.method =='GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
    })
    else:
        user = authenticate(
            request, username=request.POST['username'],password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'USUARIO O CONTRASEÑA INCORRECTA'
            })
        else:
            login(request, user)
            return redirect('core:home')

# Vistas para el CRUD del modelo Cargo

@login_required
def create_cargo(request):

    if request.method == 'POST':
        form = CargoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:list_cargo')
    else:
        form = CargoForm()
    return render(request, 'Cargo/create_cargo.html', {'form': form})


@login_required
def mostrar_cargos(request):
    query = request.GET.get('q')
    if query:
        cargos = Cargo.objects.filter(descripcion__icontains=query)
    else:
        cargos = Cargo.objects.all()

    paginator = Paginator(cargos, 4)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Cargo/list.html', {
        'cargos': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj
    })

@login_required
def delete_cargo(request, id):
    cargo = get_object_or_404(Cargo, id=id)
    cargo.delete()
    return redirect('core:list_cargo')


@login_required
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
@login_required
def create_departamento(request):

    if request.method == 'POST':
        form = DepartamentoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:list_departamento')
    else:
        form = DepartamentoForm()
    return render(request, 'Departamento/create_departamento.html', {'form': form})


@login_required
def mostrar_departamentos(request):
    query = request.GET.get('q')
    if query:
        departamentos = Departamento.objects.filter(descripcion__icontains=query)
    else:
        departamentos = Departamento.objects.all()

    paginator = Paginator(departamentos, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Departamento/list.html', {
        'departamentos': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj
    })

@login_required
def delete_departamento(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    departamento.delete()
    return redirect('core:list_departamento')


@login_required
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

@login_required
def create_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:list_empleado')
    else:
        form  = EmpleadoForm()
    return render(request, 'Empleado/create_empleado.html', {'form': form})

@login_required
def mostrar_empleado(request):
    query = request.GET.get('q')
    if query:
        empleado = Empleado.objects.filter(cedula__icontains=query)
    else:
        empleado = Empleado.objects.all()

    paginator = Paginator(empleado, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Empleado/list.html', {
        'empleados': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj
    })

def delete_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect('core:list_empleado') 

@login_required
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

@login_required
def mostrar_rol(request):
    query = request.GET.get('q')
    if query:
        rols = Rol.objects.filter(Empleado__icontains=query)
    else:
        rols = Rol.objects.all()
    return render(request, 'Rol/list.html', {'roles': rols})

@login_required
def create_rol(request):
    context={'title':'Crear Rol de pago'}
    if request.method == 'GET':
        form = RolForm()
        context['form'] = form
        return render(request, 'Rol/create_rol.html', context)
    else:
        form  = RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:list_rol')
        else:
            context['form'] = form
            return render(request, 'Rol/create_rol.html')
        

@login_required
def update_rol(request,id):
    context = {'title': 'Actualizar Rol'}

    rol = Rol.objects.get(pk=id)
    
    if request.method == "GET":
        form = RolForm(instance=rol)
        context['form'] = form
        return render(request, 'Rol/create_rol.html',context)
    else:
        form = RolForm(request.POST,instance=rol)
        if form.is_valid():
          form.save()
          return redirect('core:list_rol')
        else:
            context['form'] = form
            return render(request,'Rol/create_rol.html',context)
      
@login_required
def delete_rol(request, id):
    rol = None
    try:
        rol = Rol.objects.get(pk=id)
        if request.method == "GET":
            context = {'title':'Rol a Eliminar','rol':rol,'error':''}
            return render (request, 'Rol/delete_rol.html',context)
        else:
            rol.delete()
            return redirect('core:list_rol')
    except:
        context= {'title' : 'Datos del rol','rol':rol,'error':'Error al eliminar el rol'}
        return render (request, 'Rol/delete_rol.html',context)

# Vistas para el CRUD del modelo Contrato

@login_required
def create_contrato(request):

    if request.method == 'POST':
        form = ContratoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('core:list_contrato')
    else:
        form = ContratoForm()
    return render(request, 'Contrato/create_contrato.html', {'form': form})


@login_required
def mostrar_contrato(request):
    query = request.GET.get('q', '')
    contrato_list = TipoContrato.objects.filter(descripcion__icontains=query) if query else TipoContrato.objects.all()

    paginator = Paginator(contrato_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'contrato': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'request': request  # para mantener el valor del input de búsqueda
    }

    return render(request, 'Contrato/list.html', context)

@login_required
def delete_contrato(request, id):
    contrato = get_object_or_404(TipoContrato, id=id)
    contrato.delete()
    return redirect('core:list_contrato')


@login_required
def update_contrato(request, id):
    contrato = get_object_or_404(TipoContrato, id=id)
    if request.method == 'POST':
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            return redirect('core:list_contrato')
    else:
        form = ContratoForm(instance=contrato)
    return render(request, 'Contrato/update_contrato.html', {'form': form})