# Generated by Django 2.2.2 on 2019-08-31 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190831_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
    ]
