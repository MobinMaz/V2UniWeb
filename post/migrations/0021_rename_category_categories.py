# Generated by Django 5.0.4 on 2024-07-11 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='category',
            new_name='Categories',
        ),
    ]
