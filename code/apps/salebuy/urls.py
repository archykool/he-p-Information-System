from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

# 正在部署的应用的名称
app_name = 'salebuy'

urlpatterns = [
    # 帖子列表
    path('salebuy-list/', views.salebuy_list, name='salebuy_list'),
    # 帖子详情
    path('salebuy-detail/<int:id>/', views.salebuy_detail, name='salebuy_detail'),
    # 用户发帖
    path('salebuy-create/', views.salebuy_create, name='salebuy_create'),
    # 删除帖子
    path('salebuy-delete/<int:id>/', views.salebuy_delete, name='salebuy_delete'),
    # 修改帖子
    path('salebuy-update/<int:id>/', views.salebuy_update, name='salebuy_update'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


