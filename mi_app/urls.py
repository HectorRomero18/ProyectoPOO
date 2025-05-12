from django.urls import path
from .import  views
app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('', views.home, name='home'),
    
    # *****************URL PARA EL MODELO CARGO**********************
    path('create_cargo', views.create_cargo, name='create_cargo'),
    path('list_cargo', views.mostrar_cargos, name='list_cargo'),
    path('delete_cargo/<int:id>', views.delete_cargo, name='delete_cargo'),
    path('update_cargo/<int:id>', views.update_cargo, name='update_cargo'),

    # *********************URL PARA EL MODELO DEPARTAMENTO**********************
    path('create_departamento', views.create_departamento, name='create_departamento'),
    path('list_departamento', views.mostrar_departamentos, name='list_departamento'),
    path('delete_departamento/<int:id>', views.delete_departamento, name='delete_departamento'),
    path('update_departamento/<int:id>', views.update_departamento, name='update_departamento')
]

