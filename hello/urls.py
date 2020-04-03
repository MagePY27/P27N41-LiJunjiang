from django.urls import path, re_path
from . import views

# 普通传参 url 基本和无参数一样
    # 访问方法：http://IP:PORT/date/?year=2019&month=06
    # path("", views.date, name="date"),

    # 关键字传参   (?<参数名>参数类型)  在视图中直接通过参数名获取值
    # 访问方法：http://IP:PORT/date/2019/06/
    # re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/", views.date, name="date"),

    # 位置匹配
    # 访问方法： http://IP:PORT/date/2019/06/
    # re_path('([0-9]{4})/([0-9]{2})/', views.date, name="date"),


app_name = 'hello'

urlpatterns = [
    # path('hello', views.index, name='index'),
    path('',  views.userlist,  name='list'),
    path('create/', views.create, name="create"),
    path('edit/', views.edit, name='edit')


]

