# Generated by Django 4.2.18 on 2025-01-20 04:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_collaborationrequest_user_alter_about_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
