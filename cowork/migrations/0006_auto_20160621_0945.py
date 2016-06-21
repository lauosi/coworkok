# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import cowork.models


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0005_auto_20160620_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(width_field='width_field', null=True, upload_to=cowork.models.upload_logo, blank=True, height_field='height_field'),
        ),
        migrations.AlterField(
            model_name='desk',
            name='rent_end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 21, 9, 45, 15, 515467, tzinfo=utc)),
        ),
    ]
