# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-15 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20161102_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_auth',
            field=models.SmallIntegerField(choices=[(0, '全员可见'), (1, '仅登录可见')], default=0, verbose_name='阅读权限'),
        ),
    ]
