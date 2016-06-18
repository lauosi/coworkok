# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, width_field='width_field', height_field='height_field', null=True, upload_to='logo'),
        ),
        migrations.AddField(
            model_name='company',
            name='vat_id',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^\\d{10}$')], blank=True, verbose_name='VAT-ID', null=True, max_length=10),
        ),
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
