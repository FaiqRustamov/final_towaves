# Generated by Django 2.2.2 on 2019-08-31 14:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190831_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 8, 31, 14, 27, 5, 851005, tzinfo=utc), max_length=255),
        ),
    ]
