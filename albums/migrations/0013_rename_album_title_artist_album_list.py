# Generated by Django 4.2.1 on 2023-05-29 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0012_artist_album_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='album_title',
            new_name='album_list',
        ),
    ]