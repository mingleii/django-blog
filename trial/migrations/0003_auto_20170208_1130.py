# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trial', '0002_auto_20161115_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to='upload/', verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='uploadfile',
            name='name',
            field=models.CharField(blank=True, max_length=255, verbose_name='名称'),
        ),
    ]