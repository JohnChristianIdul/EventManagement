# Generated by Django 4.2.5 on 2023-09-17 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='specialization',
        ),
    ]
