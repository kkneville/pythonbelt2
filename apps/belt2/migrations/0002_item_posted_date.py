# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 18:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='posted_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
