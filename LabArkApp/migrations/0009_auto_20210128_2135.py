# Generated by Django 3.1.2 on 2021-01-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabArkApp', '0008_profile_userpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.TextField(default='Мой первый статус!', max_length=100),
        ),
        migrations.AlterField(
            model_name='lab',
            name='variant',
            field=models.CharField(default=0, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='year',
            field=models.IntegerField(default=2021),
        ),
    ]
