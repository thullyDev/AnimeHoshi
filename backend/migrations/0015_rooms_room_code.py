# Generated by Django 5.0.1 on 2024-02-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_code',
            field=models.CharField(default=None, max_length=7),
        ),
    ]
