# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-03 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('blood_group', models.CharField(max_length=264)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('phone', models.CharField(max_length=264)),
                ('email_id', models.EmailField(max_length=264)),
                ('medicalHistory', models.TextField()),
                ('a1', models.IntegerField()),
                ('a2', models.IntegerField()),
                ('a3', models.IntegerField()),
                ('a4', models.IntegerField()),
                ('a5', models.IntegerField()),
                ('a6', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('email_id', models.EmailField(max_length=264)),
                ('Designation', models.CharField(max_length=264)),
                ('phone', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('blood_group', models.CharField(max_length=264)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('phone', models.CharField(max_length=264)),
                ('email_id', models.CharField(max_length=264)),
                ('medicalHistory', models.TextField()),
                ('a1', models.IntegerField()),
                ('a2', models.IntegerField()),
                ('a3', models.IntegerField()),
                ('a4', models.IntegerField()),
                ('a5', models.IntegerField()),
                ('a6', models.IntegerField()),
            ],
        ),
    ]
