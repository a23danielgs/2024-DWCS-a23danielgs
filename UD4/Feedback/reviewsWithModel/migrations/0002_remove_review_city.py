# Generated by Django 4.2.18 on 2025-01-31 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsWithModel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='city',
        ),
    ]
