# Generated by Django 3.0.6 on 2020-06-01 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20200601_0339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='media_type',
            new_name='mediatype',
        ),
    ]
