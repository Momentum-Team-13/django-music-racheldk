# Generated by Django 4.0.5 on 2022-07-05 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='favorite',
        ),
    ]
