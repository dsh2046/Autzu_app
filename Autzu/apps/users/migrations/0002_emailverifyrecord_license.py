# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-05 19:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='code')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('send_type', models.CharField(choices=[('register', 'register'), ('forget', 'forget')], default='register', max_length=10)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'EmailVerify',
                'verbose_name_plural': 'EmailVerify',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_num', models.CharField(max_length=30, verbose_name='license_num')),
                ('driver_name', models.CharField(max_length=100, verbose_name='driver_name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add_time')),
            ],
            options={
                'verbose_name': 'License',
                'verbose_name_plural': 'License',
            },
        ),
    ]
