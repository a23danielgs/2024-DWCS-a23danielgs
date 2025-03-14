# Generated by Django 4.2.18 on 2025-02-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsWithModel', '0002_remove_review_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='role',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='sign_on',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='web',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
