# Generated by Django 4.1.2 on 2022-12-03 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiendaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nboleta', models.CharField(max_length=50)),
                ('Rutl', models.CharField(max_length=100)),
                ('DiLocal', models.CharField(max_length=100)),
                ('fecha', models.DateField(verbose_name='Fecha Compra')),
                ('telefono', models.CharField(max_length=100)),
                ('NomLocal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
    ]
