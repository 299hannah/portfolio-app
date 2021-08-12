# Generated by Django 3.2.6 on 2021-08-12 22:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
