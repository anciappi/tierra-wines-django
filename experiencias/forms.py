from django.forms import ModelForm
from .models import Experiencia

class ExpForm(ModelForm):
    class Meta:
        model = Experiencia
        fields = ['titulo', 'name', 'last_name', 'mail', 'contenido']
        
        