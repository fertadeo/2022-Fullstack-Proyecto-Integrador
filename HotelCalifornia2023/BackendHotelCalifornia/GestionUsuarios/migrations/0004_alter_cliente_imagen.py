# Generated by Django 4.2.2 on 2023-06-15 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionUsuarios', '0003_cliente_ciudad_cliente_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='img/perfil'),
        ),
    ]
