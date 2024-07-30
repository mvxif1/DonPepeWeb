# Generated by Django 5.0.6 on 2024-06-26 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_venta_direccion_delete_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('idDireccion', models.IntegerField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=20)),
                ('numero', models.IntegerField()),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='venta',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.direccion'),
        ),
    ]