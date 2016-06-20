# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0003_auto_20160618_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='location',
            field=models.ForeignKey(to='cowork.Location', related_name='desks'),
        ),
        migrations.AlterField(
            model_name='desk',
            name='owner',
            field=models.ForeignKey(null=True, related_name='desks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='desk',
            name='rent_end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 20, 11, 3, 31, 650114, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='desk',
            name='rent_start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
