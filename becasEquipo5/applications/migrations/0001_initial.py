# Generated by Django 4.1 on 2022-08-08 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0002_alter_student_zip_code'),
        ('institutions', '0004_remove_contactperson_institution_and_more'),
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.institution', verbose_name='Institución que recibe la solicitud')),
                ('scholarship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scholarships.scholarship', verbose_name='Beca que se solicita')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='Estudiante que hace la solicitud')),
            ],
            options={
                'db_table': 'applications',
            },
        ),
    ]
