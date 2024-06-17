# Generated by Django 5.0.4 on 2024-06-17 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_alter_user_studentcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='media/postCollection/')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='imageCollections',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.imagecollection'),
        ),
    ]