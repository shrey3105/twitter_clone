# Generated by Django 3.0.3 on 2020-07-31 05:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0006_auto_20200731_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 5, 15, 14, 331602, tzinfo=utc)),
        ),
    ]
