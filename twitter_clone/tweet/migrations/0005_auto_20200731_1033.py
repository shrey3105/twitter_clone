# Generated by Django 3.0.3 on 2020-07-31 05:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_auto_20200730_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 31, 5, 3, 19, 521547, tzinfo=utc)),
        ),
    ]