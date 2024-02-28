from django.urls import path, re_path
from . import views

app_name='message'

urlpatterns = [
    #消息首页
    path('', views.index, name='msg_index'),
    # 所有留言
    path('msg_showAll/', views.showAll, name='msg_showAll'),
    # 留言详情
    path('msg_detail/<int:id>', views.message_detail, name='msg_detail'),
    path('msg_succeed/', views.succeed, name='succeed'),
    #添加留言
    path('msg_add/', views.msg_post_page, name='msg_add'),
    #某个用户的留言,正则表达式\w+ 用于获取 url 请求地址中的用户名。
    re_path(r'^user_msg_list/([\w\W]*)/$', views.user_msg_list_page, name='user_msg_list'),
    #我的留言
    path('my_msg_list/', views.my_msg_list_page, name='my_msg_list'),

    # # 用户注册
    # path('register/', views.user_register, name='register'),
    # # 用户删除
    # path('delete/<int:id>/', views.user_delete, name='delete'),
]