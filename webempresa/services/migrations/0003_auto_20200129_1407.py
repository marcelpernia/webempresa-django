# Generated by Django 3.0.2 on 2020-01-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200127_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': ('servicio',), 'verbose_name_plural': ('mis servicios',)},
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
    ]
