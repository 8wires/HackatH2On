# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropchain', '0005_auto_20170512_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='typechallenge',
            name='obj',
            field=models.PositiveSmallIntegerField(default=100),
        ),
    ]