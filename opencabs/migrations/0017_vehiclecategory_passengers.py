# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-23 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0016_auto_20180110_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclecategory',
            name='passengers',
            field=models.IntegerField(blank=True, default=4),
        ),
    ]
