# Generated by Django 4.2.5 on 2023-11-19 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_rename_created_by_profile_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='user',
            new_name='created_by',
        ),
    ]
