# Generated by Django 5.0.4 on 2024-07-11 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_alter_post_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
