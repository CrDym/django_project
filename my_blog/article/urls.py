# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 16:00
# @Author  : Rock
# @File    : urls.py
# @describe:

from django.urls import path
from . import views
app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create')
]