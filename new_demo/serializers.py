from .models import Img,UserPro
from rest_framework import serializers
from django.contrib import auth
from django.contrib.auth.models import User as adminUser
class ImgSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Img
        fields=('imgname','imgurl','time','result')
class adminUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=adminUser
        fields=('username','password')
class smsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserPro
        fields=('user_id','phone','sms')