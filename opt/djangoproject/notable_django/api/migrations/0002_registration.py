# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-06 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=200)),
                ('phone_number_1', models.CharField(max_length=200)),
                ('phone_number_2', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('passcode', models.CharField(max_length=200)),
            ],
        ),
    ]
