# Generated by Django 4.2.1 on 2023-05-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0013_rename_album_title_artist_album_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(default=1, upload_to='media/images/'),
            preserve_default=False,
        ),
    ]