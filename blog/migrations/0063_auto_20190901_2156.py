# Generated by Django 2.2.2 on 2019-09-01 16:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0062_auto_20190901_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 9, 1, 16, 26, 44, 294521, tzinfo=utc), max_length=255),
        ),
    ]
