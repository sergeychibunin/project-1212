# Generated by Django 3.1.2 on 2020-11-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201101_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentaudio',
            name='audio_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
