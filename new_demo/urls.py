from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'img',views.ImgViewSet)
router.register(r'sms',views.smscodeViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('registerPage',views.registerPage,name='registerPage'),
]