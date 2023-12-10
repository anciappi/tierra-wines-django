from django.shortcuts import render
from django.http import HttpResponse
from .models import Experiencia

# Create your views here.

def experiencias(request):
    experiencias = Experiencia.objects.all()
    return render(request, 'experiencias.html', {
        'experiencias': experiencias
        
        })