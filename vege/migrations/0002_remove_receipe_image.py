# Generated by Django 5.0.7 on 2024-08-05 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='image',
        ),
    ]
