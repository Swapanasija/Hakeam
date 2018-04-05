# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('blood_group', models.CharField(max_length=264)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('phone', models.CharField(max_length=264)),
                ('email_id', models.EmailField(max_length=264)),
                ('medicalHistory', models.TextField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]
