# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-10 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160806_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='blog/img', verbose_name='预览图片'),
        ),
    ]
