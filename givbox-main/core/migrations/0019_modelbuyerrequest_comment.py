# Generated by Django 4.1.10 on 2023-11-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_modeldepots_infoen_modeldepots_infokg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelbuyerrequest',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
    ]
