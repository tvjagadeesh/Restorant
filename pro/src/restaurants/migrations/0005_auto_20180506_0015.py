# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-05 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20180506_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),

    ]
