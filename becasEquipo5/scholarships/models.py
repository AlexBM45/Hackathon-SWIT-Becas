from django.db import models
from institutions.models import Institution

# Create your models here.
class Requirement(models.Model):
    gpa_min = models.IntegerField(default=0, verbose_name='Promedio mínimo')
    age_min = models.IntegerField(default=0, verbose_name='Edad mínima')
    gender = models.CharField(max_length=120, verbose_name='Género')
    area_sch = models.CharField(max_length=120, verbose_name='Área al que pertenece la beca')
    education_level = models.CharField(max_length=120, verbose_name='Nivel educativo requerido')
    english_level = models.CharField(max_length=120, verbose_name='Nivel de inglés mínimo')
    
    class Meta:
        db_table = 'requirements'
    
    def __str__(self):
        return self.education_level

class Scholarship(models.Model):
    name = models.CharField(max_length=120, verbose_name='Nombre Beca')
    area = models.CharField(max_length=56, verbose_name='Área a la que pertenece')
    modality = models.CharField(max_length=56, verbose_name='Modalidad')
    period = models.CharField(max_length=120, verbose_name='Duración de la beca')
    details = models.CharField(max_length=256, verbose_name='Descripción de la Institución')
    institution= models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, verbose_name='Institución que ofrece la beca')
    requirements = models.ForeignKey(Requirement, on_delete=models.CASCADE, null=True, verbose_name='Persona de contacto')

    class Meta:
        db_table = 'scholarships'
    
    def __str__(self):
        return self.name
