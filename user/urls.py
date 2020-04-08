from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('', views.userList, name='index'),
    path('userlist', views.userList, name='userlist'),
    path('useradd/', views.userAdd, name="useradd"),
    path('<int:user_id>/resetUser', views.setUser, name="setuser"),
    path('<int:user_id>/delUseer/', views.delUser, name='deluser'),
]