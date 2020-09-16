#!/usr/bin/env python3
# coding=utf-8
# @Time    : 2020/9/16 23:32
# @Author  : Rock
# @File    : forms.py
# @Software: PyCharm

# 引入表单类
from django import forms
# 引入文章模型
from . models import ArticlePost


# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body')
