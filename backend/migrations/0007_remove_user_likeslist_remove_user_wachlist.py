# Generated by Django 5.0.1 on 2024-02-06 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_admin_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='likeslist',
        ),
        migrations.RemoveField(
            model_name='user',
            name='wachlist',
        ),
    ]
