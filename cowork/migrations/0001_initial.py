# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='companies')),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rent_start_date', models.DateTimeField(null=True)),
                ('rent_end_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('city', models.CharField(max_length=200)),
                ('total_desks', models.IntegerField(verbose_name='Total desks')),
                ('reserved_desks', models.IntegerField(verbose_name='Reserved desks')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Price per desk $', max_digits=12)),
                ('company', models.ForeignKey(to='cowork.Company', related_name='locations')),
            ],
        ),
        migrations.AddField(
            model_name='desk',
            name='location',
            field=models.OneToOneField(to='cowork.Location', related_name='desks'),
        ),
        migrations.AddField(
            model_name='desk',
            name='owner',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='desks', null=True),
        ),
    ]
