# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 14:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_member_dob'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='dob',
            new_name='hired',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='email',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lastname',
        ),
    ]