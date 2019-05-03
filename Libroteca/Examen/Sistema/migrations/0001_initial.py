# Generated by Django 2.1.2 on 2018-12-04 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=50)),
                ('costoPresupuestado', models.CharField(max_length=50, null=True)),
                ('costoReal', models.CharField(max_length=300, null=True)),
                ('tiendaProducto', models.CharField(max_length=100, null=True)),
                ('notaAdicional', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('perfil', models.CharField(default='Usuario', max_length=20)),
                ('rut', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]