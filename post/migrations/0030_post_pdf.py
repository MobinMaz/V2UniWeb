# Generated by Django 5.0.4 on 2024-10-05 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0029_remove_post_largecontent_largecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf/'),
        ),
    ]