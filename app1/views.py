from django.shortcuts import render,redirect
from .models import *

# Create your views here.
li = []

def login(request):
    if request.method.lower() == "post":
        get_username = request.POST.get("username")
        get_password = request.POST.get("password")

        a = user.objects.filter(username=get_username,password=get_password)

        if a:
            li.clear()
            for i in a:
                li.append(i)
            return redirect("index")

        else:
            return render(request,"login.html",{"err":"账号或密码错误!"})

    else:
        return render(request,"login.html")


def index(request):

    con = essay.objects.all()

    return render(request,"index.html",{"con":con})


def deta(request,id):
    #获取文章的id
    a = essay.objects.get(id=id)

    if request.method.lower() == "post":
        #判断用户是否登录
        if li:
            #获取发表的评论
            get_con = request.POST.get("con")
            #将用户发表的评论存入数据库
            comment.objects.create(con=get_con,c_ess_id=id,c_user_id=li[0].pk)
            #根据文章id获取对应的评论内容
            con_all = comment.objects.filter(c_ess=id)
            return render(request,"deta.html",{"a":a,"con":con_all})
        else:
            return redirect("login")

    else:
        # 根据文章id获取对应的评论内容
        con_all = comment.objects.filter(c_ess=id)
        return render(request,"deta.html",{"a":a,"con":con_all})







