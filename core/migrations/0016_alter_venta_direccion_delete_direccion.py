# Generated by Django 5.0.6 on 2024-06-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_direccion_iddireccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Direccion',
        ),
    ]
