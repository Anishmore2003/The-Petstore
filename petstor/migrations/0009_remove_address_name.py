# Generated by Django 5.0 on 2024-01-08 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petstor', '0008_address_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='name',
        ),
    ]
