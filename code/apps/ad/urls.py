from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

# 正在部署的应用的名称
app_name = 'ad'

urlpatterns = [
    # 帖子列表
    path('ad-list/', views.ad_list, name='ad_list'),
    # 帖子详情
    path('ad-detail/<int:id>/', views.ad_detail, name='ad_detail'),
    # 用户发帖
    path('ad-create/', views.ad_create, name='ad_create'),
    # 删除帖子
    path('ad-delete/<int:id>/', views.ad_delete, name='ad_delete'),
    # 修改帖子
    path('ad-update/<int:id>/', views.ad_update, name='ad_update'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


