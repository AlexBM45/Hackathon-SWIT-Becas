from django.db import models

# Create your models here.

class Institution(models.Model):
    # Atributos
    name = models.CharField(max_length=120, verbose_name='Nombre Institución')
    kind = models.CharField(max_length=56, verbose_name='Tipo de Institución')
    area = models.CharField(max_length=56, verbose_name='Área a la que pertenece')
    country = models.CharField(max_length=56, verbose_name='País')
    website = models.CharField(max_length=56, verbose_name='Sitio Web')
    description = models.CharField(max_length=256, verbose_name='Descripción de la Institución')

    #Nombre de la tabla:
    class Meta:
        db_table = 'institutions'
    
    #Función que imprime 'name'
    def __str__(self):
        return self.name