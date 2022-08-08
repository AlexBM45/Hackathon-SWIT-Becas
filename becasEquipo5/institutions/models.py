from django.db import models

# Create your models here.


class Institution(models.Model):
    # Atributos
    name = models.CharField(max_length=120, verbose_name='Nombre Institución')
    kind = models.CharField(max_length=56, verbose_name='Tipo de Institución')
    area = models.CharField(max_length=56, verbose_name='Área a la que pertenece')
    country = models.CharField(max_length=56, verbose_name='País')
    website = models.CharField(max_length=120, verbose_name='Sitio Web')
    description = models.CharField(max_length=256, verbose_name='Descripción de la Institución')

    #Nombre de la tabla:
    class Meta:
        db_table = 'institutions'
    
    #Función que imprime 'name'
    def __str__(self):
        return self.name


class ContactPerson(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre de la persona de contacto')
    phone = models.BigIntegerField(default=0, verbose_name='Número de teléfono')
    email = models.EmailField(max_length=120, verbose_name='Correo electrónico')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name='Institución a la que pertenece')

    class Meta:
        db_table = 'contactpersons'

    def __str__(self):
        return self.name
        