# Generated by Django 4.1.10 on 2024-01-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_modelitem_colors_modelitem_gender_modelitem_memory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelitem',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужской'), ('female', 'Женский'), ('kids', 'Детский')], default='male', max_length=30, verbose_name='Пол'),
        ),
    ]