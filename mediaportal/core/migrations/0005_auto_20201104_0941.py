# Generated by Django 3.1.2 on 2020-11-04 09:41

from django.db import migrations
import sortedm2m.fields
from sortedm2m.operations import AlterSortedManyToManyField


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201101_1410'),
    ]

    operations = [
        AlterSortedManyToManyField(
            model_name='page',
            name='texts',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='core.ContentText'),
        ),
    ]
