from django.shortcuts import render, redirect, HttpResponse
import requests
import json
import base64
from .models import FaceModel


# Create your views here.


def get_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id' \
          '=FEXN5AAS5nkGL7OcDpgk8i1D&client_secret=enRaqMYUn25S4tIh5XewdoeHnLb7Gb5G'

    # 向百度服务器发起一个请求, 获取响应
    a = requests.post(url=url)

    return a.json().get('access_token')


def reg(request):
    if request.method.lower() == "post":

        pic = request.POST.get('pic')

        url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add?access_token=%s' % get_token()
        header = {"Content-Type": "application/json"}
        body = {
            "image": pic[23:],
            "image_type": "BASE64",
            "group_id": "wasai",
            "user_id": "L"
        }

        r = requests.post(url=url, data=body, headers=header)

        return HttpResponse(r)

    else:

        return render(request, "ai/face_r.html")


def sea(request):
    if request.method.lower() == 'post':

        pic = request.POST.get('pic')

        url = 'https://aip.baidubce.com/rest/2.0/face/v3/search?access_token=%s' % get_token()

        header = {"Content-Type": "application/json"}

        body = {
            "image": pic[23:],
            "image_type": "BASE64",
            "group_id_list": "icon",
        }

        r = requests.post(url=url, data=body, headers=header)

        return HttpResponse(r)

    else:

        return render(request, 'ai/face_s.html')


def live(request):
    if request.method.lower() == 'post':

        pic = request.POST.get('pic')

        url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceverify?access_token=%s' % get_token()

        header = {"Content-Type": "application/json"}

        body = [{
            "image": pic[23:],
            "image_type": "BASE64",
            "face_field": "age,beauty,expression,face_shape,gender,glasses,race,face_type"
        }]

        body1 = json.dumps(body)

        r = requests.post(url=url, data=body1, headers=header)

        return HttpResponse(r)

    else:

        return render(request, 'ai/face_l.html')



def get_pic(request,face):

    get_pic = request.FILES.get(face)

    picmodel = FaceModel(pic=get_pic)

    picmodel.save()

    f = open(str(picmodel.pic),'rb')

    b64_pic = base64.b64encode(f.read())

    return str(b64_pic,'utf-8')

def many(request):
    if request.method.lower() == 'post':

        url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceverify?access_token=%s' % get_token()

        header = {"Content-Type": "application/json"}

        body = [
            {
                'image':get_pic(request,'face1'),
                'image_type':'BASE64',
                "face_field": "age,beauty,expression,face_shape,gender,glasses,race,face_type"
            },{
                'image': get_pic(request, 'face2'),
                'image_type': 'BASE64',
                "face_field": "age,beauty,expression,face_shape,gender,glasses,race,face_type"
            },{
                'image': get_pic(request, 'face3'),
                'image_type': 'BASE64',
                "face_field": "age,beauty,expression,face_shape,gender,glasses,race,face_type"
            }
        ]
        body1 = json.dumps(body)

        r = requests.post(url=url, data=body1, headers=header)

        return HttpResponse(r)

    else:

        return render(request, 'ai/face_m.html')
