# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-10 10:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180208_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='help',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='help',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='help',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='help',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='help',
            name='location',
        ),
        migrations.RemoveField(
            model_name='help',
            name='medicalHistory',
        ),
        migrations.RemoveField(
            model_name='help',
            name='phone',
        ),
    ]
