# Generated by Django 3.1.3 on 2020-12-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabArkApp', '0004_auto_20201215_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='upload_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
