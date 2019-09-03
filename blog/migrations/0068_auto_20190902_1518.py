# Generated by Django 2.2.2 on 2019-09-02 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0067_auto_20190902_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Music', 'Music'), ('Rock', 'Rock'), ('Jazz', 'Jazz')], default='green', max_length=5),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.CharField(default=datetime.datetime(2019, 9, 2, 9, 48, 18, 724139, tzinfo=utc), max_length=255),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
