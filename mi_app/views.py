from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from .models import Cargo
from .forms import CargoForm


def home(request):
    data = {
        'title': 'APP DE NO SE QUE',
        'description': 'Gesion de citas medicas',
        'author': 'Daniel Vera',
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



