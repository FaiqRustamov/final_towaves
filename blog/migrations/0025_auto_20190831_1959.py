# Generated by Django 2.2.2 on 2019-08-31 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20190831_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 8, 31, 14, 29, 56, 580373, tzinfo=utc), max_length=255),
        ),
    ]
