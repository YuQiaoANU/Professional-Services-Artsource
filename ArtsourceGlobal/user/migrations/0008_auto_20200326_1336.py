# Generated by Django 2.2.4 on 2020-03-26 02:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200326_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 26, 13, 36, 41, 158265), verbose_name='sendTime'),
        ),
        migrations.AlterField(
            model_name='user',
            name='artist',
            field=models.BooleanField(default=True),
        ),
    ]
