# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0004_auto_20150508_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desk',
            name='location',
            field=models.ForeignKey(related_name='desks', to='cowork.Location'),
        ),
    ]
