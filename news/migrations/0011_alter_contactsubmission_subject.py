# Generated by Django 4.2.18 on 2025-01-21 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_contactsubmission_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsubmission',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
