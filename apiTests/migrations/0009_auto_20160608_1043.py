# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-08 02:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTests', '0008_remove_apidata_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apidata',
            name='isSystem',
            field=models.IntegerField(default=0, max_length=4),
        ),
    ]
