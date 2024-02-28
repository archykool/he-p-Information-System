from django.conf.urls import url, include # 这个必须导入
from django.urls import path
from news import views  # 导入.models文件中定义的方法


app_name = 'news'

urlpatterns =[
    url('seek',views.seek,),
    #url(r'^report/', views.report, name='report'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^adv/', views.adv, name='adv'),
    url(r'^lost/', views.lost, name='lost'),
    url(r'^seek/', views.seek, name='seek'),
    url(r'^sale/', views.sale, name='sale'),
    url(r'^inform/', views.inform, name='inform'),
    url(r'^xuegong/', views.xuegong, name='xuegong'),
    url(r'^qingchun/', views.qingchun, name='qingchun'),
    url(r'^xiaoche/', views.xiaoche, name='xiaoche'),
    url(r'^zxsj/', views.zxsj, name='zxsj'),
    url(r'^xiaoli/', views.xiaoli, name='xiaoli'),
    url(r'^inform_detail/(?P<inform_id>[0-9]+)/$', views.inform_detail, name="inform_detail"),
    url(r'^xuegong_detail/(?P<xuegong_id>[0-9]+)/$', views.xuegong_detail, name="xuegong_detail"),
    url(r'^qingchun_detail/(?P<qingchun_id>[0-9]+)/$', views.qingchun_detail, name="qingchun_detail"),
    path('daily/', views.daily, name='daily'),
    path('contact-create/', views.contact_create, name='contact_create'),
    url(r'^user/', views.user_inform, name='user'),
    url(r'^$', views.dashboard),
]