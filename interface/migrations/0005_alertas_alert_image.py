# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-20 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0004_auto_20171217_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertas',
            name='alert_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%D'),
        ),
    ]
