# Generated by Django 3.2.6 on 2021-09-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=30)),
                ('estado', models.BooleanField(verbose_name='true')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=20)),
                ('telefono', models.IntegerField(max_length=22)),
                ('estado', models.BooleanField(verbose_name='true')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
    ]