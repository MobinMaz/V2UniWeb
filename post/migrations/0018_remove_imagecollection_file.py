# Generated by Django 5.0.4 on 2024-06-17 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_imagecollection_file_imagecollection_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecollection',
            name='file',
        ),
    ]