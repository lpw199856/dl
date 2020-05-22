from django.db import models
from django.contrib.auth.models import User
class UserPro(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.BigIntegerField("电话号码")
    sms   = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.user.username
class Img(models.Model):
    kind = models.CharField(max_length=50,blank=True)
    imgname = models.CharField(max_length=50,blank=True)
    imgurl = models.FileField(upload_to="img/")
    time = models.DateTimeField(auto_now=True)
    result  = models.CharField(max_length=50,blank=True)
# Create your models here.
