# Generated by Django 3.0.3 on 2020-07-30 16:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 16, 42, 55, 622904, tzinfo=utc)),
        ),
    ]