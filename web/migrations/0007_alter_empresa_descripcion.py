# Generated by Django 3.2 on 2023-07-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_empresa_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='descripcion',
            field=models.CharField(max_length=50),
        ),
    ]
