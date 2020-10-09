# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 10:20
# @Author  : Rock
# @File    : forms.py
# @describe: 表单

from django import forms
from  .models import Profile

from django.contrib.auth.models import User


# 登录表单，继承了 forms.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')
