# Generated by Django 4.1 on 2022-08-07 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0002_contactperson_alter_institution_website_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa_min', models.IntegerField(default=0, verbose_name='Promedio mínimo')),
                ('age_min', models.IntegerField(default=0, verbose_name='Edad mínima')),
                ('gender', models.CharField(max_length=120, verbose_name='Género')),
                ('area_sch', models.CharField(max_length=120, verbose_name='Área al que pertenece la beca')),
                ('education_level', models.CharField(max_length=120, verbose_name='Nivel educativo requerido')),
                ('english_level', models.CharField(max_length=120, verbose_name='Nivel de inglés mínimo')),
            ],
            options={
                'db_table': 'requirements',
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nombre Beca')),
                ('area', models.CharField(max_length=56, verbose_name='Área a la que pertenece')),
                ('modality', models.CharField(max_length=56, verbose_name='Modalidad')),
                ('period', models.CharField(max_length=120, verbose_name='Duración de la beca')),
                ('details', models.CharField(max_length=256, verbose_name='Descripción de la Institución')),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.institution', verbose_name='Institución que ofrece la beca')),
                ('requirements', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scholarships.requirement', verbose_name='Persona de contacto')),
            ],
            options={
                'db_table': 'scholarships',
            },
        ),
    ]
