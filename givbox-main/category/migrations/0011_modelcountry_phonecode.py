# Generated by Django 4.1.10 on 2023-11-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0010_alter_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelcountry',
            name='phoneCode',
            field=models.CharField(blank=True, max_length=100, verbose_name='Код телефона'),
        ),
    ]