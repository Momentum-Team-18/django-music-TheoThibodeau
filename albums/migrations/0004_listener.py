# Generated by Django 4.2.1 on 2023-05-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_publisher_options_album_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
