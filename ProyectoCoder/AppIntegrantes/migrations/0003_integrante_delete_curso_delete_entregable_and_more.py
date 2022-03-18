# Generated by Django 4.0.3 on 2022-03-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppIntegrantes', '0002_remove_curso_id_remove_estudiante_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('nombre', models.CharField(max_length=40)),
                ('dni', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]