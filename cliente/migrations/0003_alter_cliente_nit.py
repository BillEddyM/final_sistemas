# Generated by Django 4.0 on 2022-11-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_telefonocliente_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=models.CharField(blank=True, default='C/F', max_length=10, null=True, verbose_name='NIT'),
        ),
    ]
