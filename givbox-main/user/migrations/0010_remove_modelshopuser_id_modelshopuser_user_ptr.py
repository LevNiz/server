# Generated by Django 4.1.10 on 2023-11-22 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_modelshopuser_alter_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelshopuser',
            name='id',
        ),
        migrations.AddField(
            model_name='modelshopuser',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]