# Generated by Django 4.1.10 on 2023-10-13 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_modelcurrency'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256, verbose_name='Адрес')),
                ('isDepot', models.BooleanField(default=True, verbose_name='Склад')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.modelcity', verbose_name='Город')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.modelcountry', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]