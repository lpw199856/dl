import requests
import base64
import json
from django.http import HttpResponse,JsonResponse
from .models import Img,UserPro
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ImgSerializer,adminUserSerializer,smsSerializer
from rest_framework import mixins
from demo1.settings import BASE_DIR
import os
import jwt
from datetime import datetime,timedelta
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
# encoding:utf-8
import requests
import random
from urllib3 import encode_multipart_formdata
from rest_framework.views import APIView
# client_id 为官网获取的AK， client_secret 为官网获取的SK
def hello(request):
    return JsonResponse({'result':200 , 'msg': '链接成功'})
def registerPage(request):
    return render(request,"register.html")
def tokencreated(name ,pwd):
    dic = {
            'exp': datetime.now() +  timedelta(days=1),
            'iat': datetime.now(),
            'iss':'gogogogo',
            'data': {
                'name':name,
                'pwd':pwd,
                'root':1,
                },
            }
    s =jwt.encode(dic,'secret',algorithm='HS256').decode('utf-8')
    return s
def tokencreated2(name,pwd):
    dic2 = {
        'exp': datetime.now() + timedelta(days=7),
        'iat': datetime.now(),
        'iss': 'gogogogo',
        'data': {
            'name': name,
            'pwd': pwd,
            'root': 1,
        },
    }
    print("ss")
    ss = jwt.encode(dic2, 'secret', algorithm='HS256').decode('utf-8')
    return ss
class UserViewSet(
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = adminUserSerializer
    def put(self, request, *args, **kwargs):
        project=request.data['project']
        print(project)
        if project=="1":
            ret = {'code': 1001, 'msg': '用户名或密码错误','loginon':'false'}
            name=request.data['username']
            print(name)
            pwd= request.data['password']
            token= request.data['token']
            token2=request.data['token2']
            print(token2)
            print(token)

            if token:
                try:
                    s = jwt.decode(token, 'secret', issuer='gogogogo', algorithms=['HS256'])  # 解密，校验签名
                    if(s['data']['name']==name and s['data']['pwd']==pwd):
                        ret['code'] = '1000'
                        ret['msg'] = '登录成功'
                        ret['token'] = token
                        ret['loginon']='true'
                        print("1")
                except:
                    try:
                        s = jwt.decode(token2, 'secret', issuer='gogogogo', algorithms=['HS256'])  # 解密，校验签名
                        if (s['data']['name'] == name and s['data']['pwd'] == pwd):
                            token=tokencreated(name,pwd)
                            ret['code'] = '1000'
                            ret['msg'] = '登录成功'
                            ret['token'] = token
                            ret['loginon'] = 'true'
                            ret['token2']=token2
                            print("2")
                    except:
                        print('a')
                        user = auth.authenticate(request, username=name, password=pwd)
                        if user:
                            token=tokencreated(name,pwd)
                            token2 = tokencreated2(name, pwd)
                            ret['code'] = '1000'
                            ret['msg'] = '登录成功'
                            ret['token'] = token
                            ret['loginon']='true'
                            ret['token2'] = token2
            else:
                user = auth.authenticate(request, username=name, password=pwd)
                print("2")
                if user:
                    s = tokencreated(name, pwd)
                    token2 = tokencreated2(name, pwd)
                    ret['code']='1000'
                    ret['msg']='登录成功'
                    ret['token'] =s
                    ret['token2'] = token2
                    ret['loginon']='true'
            return JsonResponse(ret)
        if  project=="2":
            ret = {'code': 1002, 'msg': '验证码错误或为无权限的手机号，请修改', 'loginon': 'false'}
            thephone = request.data['phone']
            thesms = request.data['sms']
            a=UserPro.objects.get(phone=thephone)
            if a.sms==thesms:
                ret['code'] = '1000'
                ret['msg'] = '登录成功'
                ret['loginon'] = 'true'
                a.sms='sssssuika'
                a.save()
            return JsonResponse(ret)
class ImgViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    queryset = Img.objects.all()
    serializer_class = ImgSerializer
    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'format': self.format_kwarg,
            'view': self
        }
    def create(self,request,*args,**kwargs):
            name=request.data['imgname']
            serializer=self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            #self.perform_create(serializer)
            post=Img.objects.get(imgname=name)
            print(post.imgurl.url)
            url = "https://api.imgbb.com/1/upload"
            payload = {'key': 'f52e916e24c25396b40c380a186d065c'}
            files = [
                ('image', open(post.imgurl.url, 'rb'))
            ]
            headers = {}
            a = requests.request("POST", url, data=payload, files=files)
            a=json.loads(a.text)
            imgurl=a['data']['url']
            print(imgurl)
            url2 = "http://49.232.156.145/predict"
            print(name)
            keys=['url','date']
            keys0=['name','data']
            value=[imgurl,str(datetime.now())]
            dict1 = dict(zip(keys,value))
            value0=[name,dict1]
            dict2 = dict(zip(keys0,value0))
            json1=json.dumps(dict2)
            print(json1)
            response = requests.request("POST", url2, data=json1)
            #print(response.text.encode('utf8'))

            #b = json.load(b.text)
           # print(b)
           # post.result="test"
           # post.save()
            return HttpResponse(response)
            #headers = self.get_success_headers(serializer.data)
class smscodeViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = UserPro.objects.all()
    serializer_class = smsSerializer
    def put(self, request, *args, **kwargs):
        # !/usr/bin/env python
        # coding=utf-8
        print(request)
        phone=request.data['phone']
        client = AcsClient('LTAI4G4zWvN2AeVYdDvxhivu', 'BUtSRanKYPgrDtLacOpkqj5HQi2OGO', 'cn-hangzhou')
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')
        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', phone)
        request.add_query_param('SignName', "识别管理程序")
        request.add_query_param('TemplateCode', "SMS_190281003")
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(random.choice(seeds))
        round="".join(random_str)
        request.add_query_param('TemplateParam', {"code":round})
        a=UserPro.objects.get(phone=phone)
        a.sms=round
        a.save()
        response = client.do_action(request)
        # python2:  print(response)
        print(str(response, encoding='utf-8'))
        return HttpResponse(response)
        # Create your views here.

