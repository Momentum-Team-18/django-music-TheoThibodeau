# Generated by Django 4.2.1 on 2023-05-30 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0017_alter_album_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='label',
        ),
    ]
