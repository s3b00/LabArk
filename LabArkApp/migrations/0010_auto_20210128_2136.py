# Generated by Django 3.1.2 on 2021-01-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabArkApp', '0009_auto_20210128_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='variant',
            field=models.CharField(default='Без варианта', max_length=20),
        ),
    ]