from django.urls import path, include
from .views import HomeView, BodegaView, VarietalesView, ContactoView, RegisterView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('bodega/', BodegaView.as_view(), name='bodega'),
    path('varietales/', VarietalesView.as_view(), name='varietales'),
    path('contacto/', ContactoView.as_view(), name='contacto'),

    #REGISTRO
    path("register/", RegisterView.as_view(), name="registro"),

]