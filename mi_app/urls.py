from django.urls import path
from .import  views
app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('', views.home, name='home'),
    
    # *****************URL PARA EL MODELO CARGO**********************
    path('create_cargo', views.create_cargo, name='create_cargo'),
    path('list_cargo', views.mostrar_cargos, name='list_cargo'),
    path('delete_cargo/<int:id>', views.delete_cargo, name='delete_cargo'),
    path('update_cargo/<int:id>', views.update_cargo, name='update_cargo')

    # *********************                       **********************

]

