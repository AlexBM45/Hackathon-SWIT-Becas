from django.db import models
from institutions.models import Institution
from scholarships.models import Scholarship
from students.models import Student

# Create your models here.
class Application(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, null=True, verbose_name='Beca que se solicita')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, verbose_name='Estudiante que hace la solicitud')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, null=True, verbose_name='Institución que recibe la solicitud')
        
    class Meta:
        db_table = 'applications'

    #def __str__(self):
    #    return self.date
