from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')

def bodega(request):
    return render(request, 'core/bodega.html')

def varietales(request):
    return render(request, 'core/varietales.html')

def contacto(request):
    return render(request, 'core/contacto.html')





# Create your views here.
