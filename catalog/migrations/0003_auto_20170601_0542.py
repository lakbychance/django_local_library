# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170601_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
