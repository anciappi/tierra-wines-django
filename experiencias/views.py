from django.shortcuts import render
from django.http import HttpResponse
from .models import Experiencia

# Create your views here.

def experiencias(request):
    if (request.method == 'POST'):
        print("mensaje enviado")
    exp = Experiencia.objects.all()
    return render(request, 'experiencias/experiencias.html', {
        'exp': exp
        
        })