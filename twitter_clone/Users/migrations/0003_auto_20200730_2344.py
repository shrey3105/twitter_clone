# Generated by Django 3.0.3 on 2020-07-30 18:14

import Users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20200730_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, max_length=1000, upload_to=Users.models.upload_to),
        ),
    ]
