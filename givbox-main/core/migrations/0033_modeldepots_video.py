# Generated by Django 4.1.10 on 2024-01-17 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_modelrequests_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeldepots',
            name='video',
            field=models.TextField(blank=True, verbose_name='Видео'),
        ),
    ]