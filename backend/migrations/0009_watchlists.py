# Generated by Django 5.0.1 on 2024-02-06 20:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_alter_user_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(unique=True)),
                ('email', models.CharField(max_length=80, unique=True)),
                ('anime_title', models.CharField(max_length=200)),
                ('watch_type', models.CharField(max_length=10)),
                ('anime_image', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]
