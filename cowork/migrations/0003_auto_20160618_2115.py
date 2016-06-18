# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0002_auto_20160618_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.CharField(max_length=6, blank=True, validators=[django.core.validators.RegexValidator('^\\d\\d-\\d\\d\\d$')], null=True),
        ),
    ]
