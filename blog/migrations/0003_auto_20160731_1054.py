# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-31 10:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20160730_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(blank=True, max_length=54, null=True, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='预览图片'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
    ]
