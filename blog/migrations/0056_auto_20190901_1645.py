# Generated by Django 2.2.2 on 2019-09-01 11:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0055_auto_20190901_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 9, 1, 11, 15, 42, 261153, tzinfo=utc), max_length=255),
        ),
    ]
