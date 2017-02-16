# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-02 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('file', models.FileField(upload_to='', verbose_name='文件')),
                ('remark', models.CharField(blank=True, default='', max_length=255, verbose_name='备注')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('utime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '文件上传',
                'verbose_name_plural': '文件上传',
            },
        ),
    ]
