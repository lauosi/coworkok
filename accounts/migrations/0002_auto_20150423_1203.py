# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(default=0, choices=[(0, b'Co-working user'), (1, b'Company offers co-working services')]),
        ),
    ]
