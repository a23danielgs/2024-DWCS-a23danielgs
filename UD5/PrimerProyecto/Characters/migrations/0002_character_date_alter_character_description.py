# Generated by Django 4.2.16 on 2024-11-22 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.TextField(),
        ),
    ]
