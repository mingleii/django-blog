#!/usr/bin/env python
# coding=utf-8
"""

author = "minglei.weng@dianjoy.com"
created = "2016/8/10"
"""
REDIS_URL = "192.168.199.224:6379"
REDIS_DB = 5
# REDIS_URL = "123.206.63.56:6379"
# REDIS_DB = 0
DEBUG = True
REDIS_PASSWD = None
BACKEND_SERVER = True
APSCHEDULER = False
EMAIL_ENABLE = True
EMAIL_TEST = { 'city': '大连', 'country': '中国', 'groupid': 0, 'headimgurl': 'http://wx.qlogo.cn/mmopen/ajNVdqHZLLBOLL1ibpsStIRfUcR8ibZ6QheyA0zOd0pOy5vqO9KgY2Bn6bckicQ7vUkH7LveOCQ1Q8B4JGWm7R5bg/0', 'language': 'zh_CN', 'nickname': '未命名', 'openid': 'o-TbGwy-MllIql2Ev5_4yzkhWmL0', 'province': '辽宁', 'remark': '', 'sex': 1, 'subscribe': 1, 'subscribe_time': 1480599185, 'tagid_list': []}
EMAIL_CONFIG = {
    "title": "YUN WARNING !!!",         # 默认邮件标题
    "sender": "Yun_Warning@163.com",    # 默认发送邮箱
    "receiver": ["645008699@qq.com"],   # 默认接收邮箱，多个请使用List类型
    "server_ip": "smtp.163.com",        # 默认邮箱服务地址
    "server_port": "25",                # 默认邮箱服务端口
    "username": "Yun_Warning@163.com",  # 默认发送邮箱用户名
    "passwd": "Wml93640218"             # 默认发送邮箱密码
}
SECRET_KEY = '_h2)yhinz8af)(i)yk=!l!*=2z9b8!qjcevq(gw1+ceo7cvxb0'