# Generated by Django 4.1.10 on 2023-10-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_modelpackage_packagedata_modelpackage_tariff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelpackagedata',
            name='weight',
        ),
        migrations.AddField(
            model_name='modelpackagedata',
            name='length',
            field=models.FloatField(default=0, verbose_name='Длина'),
        ),
    ]
