# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0004_auto_20160620_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='location',
            field=models.ForeignKey(related_name='location', to='cowork.Location'),
        ),
        migrations.AlterField(
            model_name='desk',
            name='owner',
            field=models.ForeignKey(related_name='owner', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='desk',
            name='rent_end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 20, 11, 39, 3, 537748, tzinfo=utc)),
        ),
    ]
