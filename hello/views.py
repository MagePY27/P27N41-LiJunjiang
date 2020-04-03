from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse, QueryDict
from .models import User

# Create your views here.

def create(request):
    date = request.POST
    name = date.get("name")
    sex = date.get('sex')
    passwd = date.get("passwd")

    # user = User.objects.create(name=name, sex=sex, password=passwd)

    return render(request, "hello/create.html")

def delet(request):
    pass

def edit(request):

    return render(request, "hello/edit.html")

def userlist(request):
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {'users': users})

def results(request, user_id):
    try:
        user = User.objects.get(ok=user_id)
    except User.DoesNotExist:
        raise Http404("用户创建失败")
    else:
        return render(request, 'hello/results.html', {"message": "用户创建成功"})







# 普通传参 url 基本和无参数一样
# def date(request):
#     year = request.GET.get("year", "2019")
#     month = request.GET.get("month", "04")
#
#     return HttpResponse("year is {}, month is {}".format(year, month))


# 关键字传参   (?<参数名>参数类型)  在视图中直接通过参数名获取值
# def date(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get('year', '2017')
#     month = kwargs.get('month', '01')
#
#     return HttpResponse("year is {}, month is {}".format(year, month))


# 位置匹配
# def date(request, year='1998', month='01'):
#     print("year = {}, month = {}".format(year, month))
#     return HttpResponse("year is {}, month is {}".format(year, month))

# def date(request):
#     print(request.scheme)
#     print(request.method)
#     print(request.headers)
#     print(request.path)
#     print(request.META)
#     print(request.GET)
#
#     date = request.GET
#     year = date.get("year", "1111")
#     month = date.get("month", "11")
#     print('===' * 30)
#
#     if request.method == 'POST':
#         print(request.method)
#         print(request.body)
#         print(QueryDict(request.body).dict())
#         print(request.POST)
#
#         date = request.POST
#         year = date.get("year", '2222')
#         month = date.get('month', '22')
#
#     return HttpResponse('year is {}, month is {}'.format(year, month))

