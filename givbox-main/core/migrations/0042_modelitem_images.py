# Generated by Django 4.1.10 on 2024-01-25 10:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_cartitems_color_cartitems_memory_cartitems_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelitem',
            name='images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), blank=True, null=True, size=None, verbose_name='Фото'),
        ),
    ]