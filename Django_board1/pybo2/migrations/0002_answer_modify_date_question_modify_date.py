# Generated by Django 5.1.4 on 2024-12-06 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
