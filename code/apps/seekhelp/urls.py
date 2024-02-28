from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

# 正在部署的应用的名称
app_name = 'seekhelp'

urlpatterns = [
    # 帖子列表
    path('seekhelp-list/', views.seekhelp_list, name='seekhelp_list'),
    # 帖子详情
    path('seekhelp-detail/<int:id>/', views.seekhelp_detail, name='seekhelp_detail'),
    # 用户发帖
    path('seekhelp-create/', views.seekhelp_create, name='seekhelp_create'),
    # 修改帖子
    path('seekhelp-update/<int:id>/', views.seekhelp_update, name='seekhelp_update'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


