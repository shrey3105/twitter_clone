# Generated by Django 3.0.3 on 2020-08-02 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20200802_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='follow_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 2, 14, 53, 48, 609828, tzinfo=utc)),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'follows')},
        ),
    ]