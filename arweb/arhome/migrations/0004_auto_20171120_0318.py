# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arhome', '0003_auto_20171119_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='videos_subscribe',
            field=models.ManyToManyField(to='arhome.Videos'),
        ),
    ]
