from django.shortcuts import render, redirect
from .forms import RegisterForm
from users.models import MYBOOK,Resulttable
from django.db import models

def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', context={'form': form})

def index(request):
    return render(request, 'users/..//index.html')
# 为啥？


# def showregist(request):
#     pass

def recommend(request):
    return render(request, 'users/movieRecommend.html')


def insert(request):
    # try:
    #     MOVIEID = request.POST["movieid"]
    #     USERID = request.POST["userid"]
    #     RATING = request.POST["rating"]
    #     IMDBID = request.POST["imdbid"]
    # except KeyError:
    #     MOVIEID = '0'
    #     USERID = "0"
    #     RATING = "0"
    #     IMDBID = "0"
    #     # MOVIEID = "Guest"
    #     # USERID = "Guest"
    #     # RATING = "Guest"
    #     # IMDBID = "Guest"
    # MOVIEID = int(request.GET["movieId"])
    USERID = int(request.GET["userId"])
    RATING = float(request.GET["rating"])
    IMDBID = int(request.GET["imdbId"])
    # MOVIEID = request.POST.get("movieId")
    # USERID = request.POST.get("userId")
    # RATING = request.POST.get("rating")
    # IMDBID = request.POST.get("imdbId",'0')
    # NAME = request.GET['name']
    # PRICE = float(request.GET['price'])
    Resulttable.objects.create(userId = USERID,rating = RATING,imdbId = IMDBID)
    # return render(request,'index.html', {'name':NAME, 'price': PRICE})
    return render(request, 'index.html',{'userId':USERID,'rating':RATING,'imdbId':IMDBID})