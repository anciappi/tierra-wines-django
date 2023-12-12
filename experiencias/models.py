from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Experiencia(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    mail = models.EmailField(verbose_name='Mail')
    contenido = models.TextField(max_length=1000, verbose_name='Contenido')
    imagen = models.ImageField(upload_to='experiencias', null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')


    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
        ordering = ['-fecha']

    def __str__(self):
        return self.titulo + ' | ' + self.name