# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-06 20:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_restaurantlocation1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RestaurantLocation1',
        ),
    ]
