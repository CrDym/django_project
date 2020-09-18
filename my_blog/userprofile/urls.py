# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 10:43
# @Author  : Rock
# @File    : urls.py
# @describe: 用户模块url

from django.urls import path
from .import views

app_name = 'userprofile'


urlpatterns =[
    # 用户登录
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]