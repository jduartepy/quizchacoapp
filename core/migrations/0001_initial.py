# Generated by Django 3.2.6 on 2021-08-14 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.TextField()),
                ('respuesta', models.CharField(max_length=50)),
                ('opcion1', models.TextField()),
                ('opcion2', models.TextField()),
                ('opcion3', models.TextField()),
                ('opcion4', models.TextField()),
                ('categoria', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'cuestionario',
                'db_table': 'quiz',
                'ordering': ['categoria'],
            },
        ),
    ]
