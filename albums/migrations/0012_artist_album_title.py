# Generated by Django 4.2.1 on 2023-05-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0011_rename_name_artist_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='album_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
