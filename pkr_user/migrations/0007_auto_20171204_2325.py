# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 23:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pkr_user', '0006_auto_20171204_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='MSRP',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='buyPrice',
            field=models.FloatField(),
        ),
    ]