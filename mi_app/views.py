from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect


def home(request):
    data = {
        'title': 'App Medica',
        'description': 'Gesion de citas medicas',
        'author': 'Daniel Vera',
        'year': 2025,
    }
    # doctores = Doctor.objects.all()
    # data["doctores"]=doctores
    #return HttpResponse("<h1>Hello,Mi primer pagina con django</h1>")
    #return JsonResponse(data)  
    return render(request, 'home.html', data)

