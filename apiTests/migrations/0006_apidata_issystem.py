# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-08 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTests', '0005_apiname_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='apidata',
            name='isSystem',
            field=models.BooleanField(default=False),
        ),
    ]
