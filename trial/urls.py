#!/usr/bin/env python
# coding=utf-8
"""

author = "minglei.weng@dianjoy.com"
created = "2016/8/11"
"""
from django.conf.urls import url
from trial import views

urlpatterns = [
    url(r"^debug/$", views.InfoView.as_view(), name='debug'),
    url(r"^life/$", views.LifeToolsView.as_view(), name='life'),
    url(r"^just200/$", views.Just200View.as_view(), name='just200'),
]