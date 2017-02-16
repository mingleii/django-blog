#!/usr/bin/env python
# coding=utf-8
"""

author = "minglei.weng@dianjoy.com"
created = "2016/8/11"
"""
import logging
import time


logger = logging.getLogger("default")


def apscheduler_heart_beat(**kwargs):
    logger.info("apscheduler_heart_beat:BOOM~BOOM~BOOM~",
                extra=kwargs)
