# Generated by Django 4.2.5 on 2023-11-19 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='created_by',
            new_name='user',
        ),
    ]