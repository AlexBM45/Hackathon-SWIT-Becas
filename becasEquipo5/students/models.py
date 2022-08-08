from django.db import models

# Student, Address, Status_beca, Application
class Student(models.Model):
    name = models.CharField(max_length=32, verbose_name='Nombre del estudiante')
    last_name = models.CharField(max_length=32, verbose_name='Apellido del estudiante')
    email = models.EmailField(max_length=64)
    address_street = models.CharField(max_length=32, verbose_name='Calle y número')
    address_city = models.CharField(max_length=32, verbose_name='Ciudad')
    address_state = models.CharField(max_length=32, verbose_name='Estado')
    address_country = models.CharField(max_length=32, verbose_name='País')
    zip_code = models.IntegerField()
    degree = models.CharField(max_length=32, verbose_name='Nivel máximo de estudios')
    area = models.CharField(max_length=32, verbose_name='Área de estudios')

    class Meta: 
        db_table = 'students'

    def __str__(self):
        return self.name + self.last_name
