from django.shortcuts import render, get_object_or_404, Http404
from .models import User
from django.views.generic import View

# Create your views here.
def userList(request):
    kw = request.GET.get("kw", "")
    users = User.objects.all()
    if kw:
        users = User.objects.filter(name__icontains=kw)
    return render(request, 'user/list.html', {'users': users, 'kw': kw})

def userAdd(request):
    msg = {}
    print(request.method)
    if request.method == "POST":
        date = request.POST.dict()
        # print(date)
        # print(date['sex'], type(date["sex"]))
        try:
            User.objects.create(**date)
            msg = {"code": 0, "result": "添加用户成功"}
        except:
            msg = {"code": 1, "errmsg": "添加用户失败"}
        return render(request, "user/results.html", {'msg': msg})

    return render(request, "user/useradd.html")


def setUser(request, **kwargs):
    msg = {}
    pk = kwargs.get("user_id")
    print(pk)
    try:
        user = User.objects.get(pk=pk)
        print(user)
    except User.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        date = request.POST.dict()
        try:
            User.objects.filter(pk=pk).update(**date)
            msg = {'code': 0, 'result': "修改成功"}
        except:
            msg = {'code': 1, 'errmsg': "修改失败"}
        return render(request, "user/results.html", {'msg': msg})

    return render(request, "user/set.html", {'user': user, "msg": msg})

def delUser(request, **kwargs):
    msg = {}
    print(kwargs)
    pk = kwargs.get("user_id")
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == "POST":
        try:
            User.objects.filter(pk=pk).delete()
            msg = {'code': 0, "result": "删除用户成功"}
        except:
            msg = {'code': 1, "errmsg": "删除用户失败"}
        return render(request, "user/results.html", {'msg': msg})

    return render(request, "user/delete.html", {"user": user, "msg": msg})
