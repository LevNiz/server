# Generated by Django 4.1.10 on 2023-10-16 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_client_addresses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='addresses',
        ),
    ]
