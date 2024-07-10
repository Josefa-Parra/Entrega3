# Generated by Django 5.0.6 on 2024-07-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crear_Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tutor', models.CharField(max_length=40)),
                ('lugar', models.CharField(max_length=40)),
                ('dia', models.DateField()),
                ('hora', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=40)),
                ('codigo_viaje', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Participar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_viaje', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Registrarse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('ciudad', models.CharField(max_length=40)),
            ],
        ),
    ]
