# Generated by Django 5.0 on 2024-01-08 07:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petstor', '0006_product_img3'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.CharField(max_length=300, null=True)),
                ('landmark', models.CharField(max_length=200, null=True)),
                ('caty', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('pincode', models.IntegerField(null=True)),
                ('contact', models.BigIntegerField(null=True)),
                ('contactA', models.BigIntegerField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]