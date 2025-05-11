from django.urls import path
from mi_app.views import  home
app_name = 'core'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    path('', home, name='home'),

]

