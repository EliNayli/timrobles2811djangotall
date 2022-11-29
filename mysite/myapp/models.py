from django.db import models

# Create your models here.

class Persona(models.Model):
   
    nombre = models.CharField('Nombre completo',max_length=100)
    description = models.TextField('Descripción')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.nombre