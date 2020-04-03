from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('', views.userList, name='userList'),
    path('create/', views.userCreate, name="userCreate"),
    path('results/', views.results, name='results'),
    path('userInfo/', views.userInfo, name="userInfo"),
    path('<int:user_id>/getUser', views.getUser, name="getUser"),
    path('<int:user_id>/resetUser', views.resetUser, name="resetUser"),
    path('<int:user_id>/delUseer', views.delUser, name='delUser'),
]