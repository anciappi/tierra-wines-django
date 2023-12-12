from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Experiencia
from .forms import ExpForm

# Create your views here.

def experiencias(request):
    if request.method == 'GET':
        exp = Experiencia.objects.all()
        return render(request, 'experiencias/experiencias.html', {
        'exp': exp,
        'form': ExpForm,
        })
    else:
       form = ExpForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
       exp = Experiencia.objects.all()
       return render(request, 'experiencias/experiencias.html', {
        'exp': exp,
        'form': ExpForm,
        })


    