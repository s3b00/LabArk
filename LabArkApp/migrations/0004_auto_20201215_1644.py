# Generated by Django 3.1.3 on 2020-12-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabArkApp', '0003_lab_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]
