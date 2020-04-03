from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.
def userList(request):
    users = User.objects.all()
    return render(request, 'user/list.html', {'users': users})

def userInfo(request):
    return render(request, 'user/userInfo.html')

def userCreate(request):
    date = {
        'name': request.POST.get("name"),
        'password': request.POST.get("password"),
        'sex': int(request.POST.get("sex")),
    }
    if User.objects.create(**date):
    # print(user.id, type(user.id))
        return render(request, 'user/results.html', {"message": "创建成功"})
    else:
        return render(request, 'user/results.html', {"message": "创建失败"})


def getUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    date = {
        'id': user.id,
        'name': user.name,
        'password': user.password,
        'sex': user.sex
    }
    return render(request, 'user/getUser.html', date)

def resetUser(request, user_id):
    date = {
        'name': request.POST.get("name"),
        'password': request.POST.get("password"),
        'sex': request.POST.get("sex")
    }
    print(user_id, date)
    if User.objects.filter(id=user_id).update(**date):
        return render(request, 'user/results.html', {"message": "修改成功"})
    else:
        return render(request, 'user/results.html', {"message": "修改失败"})

def delUser(request, user_id):
    if User.objects.filter(id=user_id).delete():
        # if not User.objects.f
        return render(request, 'user/results.html', {'message': '删除成功'})
    else:
        return render(request, 'user/results.html', {'message': '删除失败'})



def results(request, message):
    # user = get_object_or_404(User, pk=userId)
    return render(request, 'user/results.html', {"message":message})