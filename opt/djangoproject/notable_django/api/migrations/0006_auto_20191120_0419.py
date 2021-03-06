# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-20 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='otp',
            name='shop_code',
            field=models.CharField(default=b'', editable=False, max_length=8),
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_description',
            field=models.CharField(default=b'', editable=False, max_length=200),
        ),
    ]
