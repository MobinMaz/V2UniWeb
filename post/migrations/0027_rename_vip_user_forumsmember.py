# Generated by Django 5.0.4 on 2024-07-11 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0026_rename_adminstutus_user_admin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='vip',
            new_name='ForumsMember',
        ),
    ]
