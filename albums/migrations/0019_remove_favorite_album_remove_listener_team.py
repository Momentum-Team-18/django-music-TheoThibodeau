# Generated by Django 4.2.1 on 2023-05-30 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0018_remove_album_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='album',
        ),
        migrations.RemoveField(
            model_name='listener',
            name='team',
        ),
    ]
