# Generated by Django 4.1 on 2022-09-04 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_question_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='followers',
            new_name='following_users',
        ),
    ]
