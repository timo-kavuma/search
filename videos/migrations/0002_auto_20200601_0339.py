# Generated by Django 3.0.6 on 2020-06-01 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='actor',
            new_name='actors',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='date_added',
            new_name='dateadded',
        ),
        migrations.RemoveField(
            model_name='video',
            name='views',
        ),
    ]
