# Generated by Django 2.2.2 on 2019-08-31 20:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0047_auto_20190901_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 8, 31, 20, 18, 11, 726198, tzinfo=utc), max_length=255),
        ),
    ]
