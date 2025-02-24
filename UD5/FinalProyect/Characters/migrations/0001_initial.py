# Generated by Django 4.2.18 on 2025-02-24 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='universes')),
                ('date_of_creation', models.DateField()),
                ('creator', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='characters')),
                ('alternateImage', models.ImageField(null=True, upload_to='characters')),
                ('slug', models.SlugField(unique=True)),
                ('universe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='Characters.universe')),
            ],
        ),
    ]
