# Generated by Django 4.2.16 on 2024-11-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0002_character_date_alter_character_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='alternateImage',
            field=models.ImageField(blank=True, upload_to='Characters/images/'),
        ),
    ]
