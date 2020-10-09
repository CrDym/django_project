from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.http import HttpResponse
from .forms import UserLoginForm
from .forms import ProfileForm
from .models import Profile

# 登录
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user :
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request,user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码错误")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == "GET":
        user_login_form = UserLoginForm
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 退出
def user_logout(request):
    logout(request)
    return redirect("article:article_list")


# 编辑用户信息
@login_required(login_url='/userprofile/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)

    # # user_id是 OneToOneField 自动生成的字段
    # profile = Profile.objects.get(user_id=id)
    if Profile.objects.filter(user_id=id).exists():
        profile = Profile.objects.get(user_id=id)
    else:
        profile = Profile.objects.create(user=user)

    if request.method == 'POST':
        # 验证修改数据着，是否未用户被人
            if request.user  != user:
                return HttpResponse('你没有权限修改次用户信息')

            profile_form = ProfileForm(data=request.POST)
            if profile_form.is_valid():
                # 取得清洗后的合法数据
                profile_cd = profile_form.cleaned_data
                profile.phone = profile_cd['phone']
                profile.bio = profile_cd['bio']
                profile.save()
                # 带参数的 redirect()
                return redirect("userprofile:edit", id=id)
            else:
                return HttpResponse("注册表单输入有误。请重新输入~")

    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = {'profile_form': profile_form, 'profile': profile, 'user': user}
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
