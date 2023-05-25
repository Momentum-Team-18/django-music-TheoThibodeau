# Generated by Django 4.2.1 on 2023-05-24 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.AddField(
            model_name='album',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='albums.publisher'),
        ),
    ]