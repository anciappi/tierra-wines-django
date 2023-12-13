from django.forms import ModelForm
from django import forms
from .models import Experiencia

class ExpForm(ModelForm):
    class Meta:
        model = Experiencia
        fields = ['titulo', 'name', 'last_name', 'contenido']
        
        