from django.urls import path
from .views import home, bodega, varietales, contacto

urlpatterns = [
    path('', home, name='home'),
    path('bodega/', bodega, name='bodega'),
    path('varietales/', varietales, name='varietales'),
    path('contacto/', contacto, name='contacto'),
]