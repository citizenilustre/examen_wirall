# Generated by Django 3.1.5 on 2021-02-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido')),
                ('direccion', models.CharField(max_length=400, verbose_name='Direccion')),
                ('dni', models.IntegerField(unique=True, verbose_name='Dni')),
            ],
            options={
                'db_table': 'Personas',
            },
        ),
    ]
