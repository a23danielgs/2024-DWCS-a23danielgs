# Generated by Django 4.2.18 on 2025-02-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0002_alter_character_alternateimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='universe',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
