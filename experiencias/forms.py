from django.forms import ModelForm
from django import forms
from .models import Experiencia

class ExpForm(ModelForm):
    # titulo = forms.CharField(label='Título')
    # name = forms.CharField(label='Nombre')
    # last_name = forms.CharField(label='Apellido')
    # mail = forms.EmailField(label='Mail')
    # contenido = forms.CharField(label='Contenido')
    class Meta:
        model = Experiencia
        fields = ['titulo', 'name', 'last_name', 'mail', 'contenido']
        
        