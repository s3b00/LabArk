# Generated by Django 3.1.2 on 2021-01-30 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LabArkApp', '0012_auto_20210130_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
