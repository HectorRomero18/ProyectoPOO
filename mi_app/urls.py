from django.urls import path
from django.contrib.auth import views as auth_views

from .import  views
app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signup, name='login'),
    path('signin/', views.signin, name='signin'),


    
    # *****************URL PARA EL MODELO CARGO**********************
    path('create_cargo', views.create_cargo, name='create_cargo'),
    path('list_cargo', views.mostrar_cargos, name='list_cargo'),
    path('delete_cargo/<int:id>', views.delete_cargo, name='delete_cargo'),
    path('update_cargo/<int:id>', views.update_cargo, name='update_cargo'),

    # *********************URL PARA EL MODELO DEPARTAMENTO**********************
    path('create_departamento', views.create_departamento, name='create_departamento'),
    path('list_departamento', views.mostrar_departamentos, name='list_departamento'),
    path('delete_departamento/<int:id>', views.delete_departamento, name='delete_departamento'),
    path('update_departamento/<int:id>', views.update_departamento, name='update_departamento'),
    
    # *********************URL PARA EL MODELO EMPLEADO**********************
    path('create_empleado', views.create_empleado, name='create_empleado'),
    path('list_empleado', views.mostrar_empleado, name='list_empleado'),
    path('delete_empleado/<int:id>', views.delete_empleado, name='delete_empleado'),
    path('update_empleado/<int:id>', views.update_empleado, name='update_empleado'),
    
     # *********************URL PARA EL MODELO ROL**********************
    path('create_rol', views.create_rol, name='create_rol'),
    path('list_rol', views.mostrar_rol, name='list_rol'),
    path('delete_rol/<int:id>', views.delete_rol, name='delete_rol'),
    path('update_rol/<int:id>', views.update_rol, name='update_rol'),

         # *********************URL PARA EL MODELO CONTRATO**********************
    path('create_contrato', views.create_contrato, name='create_contrato'),
    path('list_contrato', views.mostrar_contrato, name='list_contrato'),
    path('delete_contrato/<int:id>', views.delete_contrato, name='delete_contrato'),
    path('update_contrato/<int:id>', views.update_contrato, name='update_contrato'),
    
      # *********************URL PARA EL MODELO PRESTAMO**********************
    path('create_prestamo', views.create_prestamo, name='create_prestamo'),
    path('list_prestamo', views.mostrar_prestamo, name='list_prestamo'),
    path('delete_prestamo/<int:id>', views.delete_prestamo, name='delete_prestamo'),
    path('update_prestamo/<int:id>', views.update_prestamo, name='update_prestamo'),
]
