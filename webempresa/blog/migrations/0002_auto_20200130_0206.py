# Generated by Django 3.0.2 on 2020-01-30 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen'),
        ),
    ]
