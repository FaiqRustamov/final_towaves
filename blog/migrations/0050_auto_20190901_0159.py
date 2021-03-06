# Generated by Django 2.2.2 on 2019-08-31 20:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_auto_20190901_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactuser',
            name='context',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contactuser',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactuser',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactuser',
            name='subject',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactuser',
            name='surname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 8, 31, 20, 29, 7, 636274, tzinfo=utc), max_length=255),
        ),
    ]
