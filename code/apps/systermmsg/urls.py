from django.urls import path, re_path
from . import views

app_name='systermmsg'

urlpatterns = [
    #消息首页
    path('', views.ListAll, name='sys_msg_list'),
    path('sys_msg_detail/<int:id>', views.sys_msg_detail, name='sys_msg_detail'),
]