from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# 正在部署的应用的名称
app_name = 'lostfound'

urlpatterns = [
    # 帖子列表
    path('lostfound-list/', views.lostfound_list, name='lostfound_list'),
    # 帖子详情
    path('lostfound-detail/<int:id>/', views.lostfound_detail, name='lostfound_detail'),
    # 用户发帖
    path('lostfound-create/', views.lostfound_create, name='lostfound_create'),
    # 删除帖子
    path('lostfound-delete/<int:id>/', views.lostfound_delete, name='lostfound_delete'),
    # 修改帖子
    path('lostfound-update/<int:id>/', views.lostfound_update, name='lostfound_update'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)