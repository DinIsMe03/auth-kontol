# Generated by Django 5.0.6 on 2024-07-04 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='logoPerusahaan',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='owner',
        ),
    ]
