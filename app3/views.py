from django.shortcuts import render,redirect
from .models import *
import random
from django.db.models import F

# Create your views here.


def login(request):
    if request.method.lower() == 'post':
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')
        if get_username and get_password:
            a = user.objects.filter(username=get_username, password=get_password)

            if a:
                # session

                # cookie

                aa = redirect('index')
                # 不能识别中文

                aa.set_cookie(key="lcm", value=get_password, max_age=20)



                return aa

                # 原                # return redirect('ho')
            else:
                return render(request, 'login.html', {"err": "账号或密码错误!"})
        else:
            return render(request, 'login.html', {'err': '请正确输入！'})
    else:
        return render(request, 'login.html')



def index(request):
    li = []
    a = news.objects.all()
    for i in a:
        li.append(i)
    b = random.shuffle(li) #洗牌 打乱顺序

    li = li[:3]
    return render(request,"app3/index.html",{'li':li})


def more(request,id):
    a = news.objects.get(pk=id)
    b = a.comment_set.all()
    if request.COOKIES.get('lcm'):
        if request.method.lower()=='post':
            con = request.POST.get('con')
            in4 = request.POST.get('in4')
            in5 = request.POST.get('in5')
            in6 = request.POST.get('in6')
            if con:
                comment.objects.create(write=con,good_num=0,c_user_id=2,c_news_id=id)
                b = a.comment_set.all()
                return render(request, 'app3/more.html', {'a': a,'yes':'发表成功！','b':b})
            elif in4:
                reply.objects.create(write_con=in4,good_num=0,r_com_id=in5,r_user_id=1)

                return render(request, 'app3/more.html', {'a': a, 'yes': '发表成功！', 'b': b})
            elif in6:
                comment.objects.filter(pk=in6).update(good_num=F('good_num')+1)
                a = news.objects.get(pk=id)
                b = a.comment_set.all()
                return render(request, 'app3/more.html', {'a': a, 'b': b})
        else:
            return  render(request, 'app3/more.html',{'a':a,'b':b})
    else:
        return  redirect("login")



