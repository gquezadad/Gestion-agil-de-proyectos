# Generated by Django 2.1.2 on 2019-06-18 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema', '0003_reservalibros'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservalibros',
            name='descripcionLibro',
        ),
        migrations.RemoveField(
            model_name='reservalibros',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='reservalibros',
            name='usuario',
        ),
    ]