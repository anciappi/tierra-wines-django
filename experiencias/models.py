from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Experiencia(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    contenido = models.TextField(max_length=1000, verbose_name='Contenido')
    imagen = models.ImageField(upload_to='experiencias', null=True, blank=True)


    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
        ordering = ['-fecha']

    def __str__(self):
        return [self.titulo, self.autor]