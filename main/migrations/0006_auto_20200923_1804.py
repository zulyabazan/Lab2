# Generated by Django 3.1 on 2020-09-23 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='dni',
            field=models.CharField(max_length=8),
        ),
    ]
