# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0006_auto_20160621_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='desk',
            name='rent_end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 22, 12, 24, 33, 617420, tzinfo=utc)),
        ),
    ]
