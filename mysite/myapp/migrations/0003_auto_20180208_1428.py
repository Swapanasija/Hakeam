# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='a1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='a2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='a3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='a4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='a5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='a6',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]