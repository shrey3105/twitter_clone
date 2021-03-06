# Generated by Django 3.0.3 on 2020-08-01 18:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0008_auto_20200731_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_date', models.DateTimeField(default=datetime.datetime(2020, 8, 1, 18, 39, 1, 185163, tzinfo=utc))),
                ('follows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='Users.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='Users.Profile')),
            ],
        ),
    ]
