# Generated by Django 2.2.2 on 2019-08-31 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_auto_20190901_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 8, 31, 19, 53, 14, 25332, tzinfo=utc), max_length=255),
        ),
    ]
