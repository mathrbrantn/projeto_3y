# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-06 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_instrutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='instrutor',
        ),
    ]
