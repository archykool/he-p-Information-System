from django.urls import path,include,re_path


from .views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, AboutusView
from .views import UpdateEmailView,MycommendView,MyproblemsView
from . import views

app_name = 'users'

urlpatterns = [
    # 用户信息
    path("info/", UserinfoView.as_view(),name='user_info'),
    # 用户图像上传
    path("image/upload/", UploadImageView.as_view(),name='image_upload'),
    # 用户个人中心修改密码
    path("update/pwd/", UpdatePwdView.as_view(),name='update_pwd'),
    # 发送邮箱验证码
    path("sendemail_code/", SendEmailCodeView.as_view(),name='sendemail_code'),
    # 修改邮箱
    path("update_email/", UpdateEmailView.as_view(),name='update_email'),
    # 我的帖子
    path("mypost/ad/",  views.ad_list,name='mypost_ad'),
    path("mypost/salebuy/", views.salebuy_list, name='mypost_salebuy'),
    path("mypost/seekhelp/", views.seekhelp_list, name='mypost_seekhelp'),
    path("mypost/lostfound/", views.lostfound_list, name='mypost_lostfound'),
    # 修改内容
    path("update_ad/<int:id>/",  views.ad_update, name='update_ad'),
    path("update_lostfound/<int:id>/",  views.lostfound_update, name='update_lostfound'),
    path("update_salebuy/<int:id>/",  views.salebuy_update, name='update_salebuy'),
    path("update_seekhelp/<int:id>/",  views.seekhelp_update, name='update_seekhelp'),
    # 删除内容
    path('ad-delete/<int:id>/', views.ad_delete, name='ad_delete'),
    path('salebuy-delete/<int:id>/', views.salebuy_delete, name='salebuy_delete'),
    path('seekhelp-delete/<int:id>/', views.seekhelp_delete, name='seekhelp_delete'),
    path('lostfound-delete/<int:id>/', views.lostfound_delete, name='lostfound_delete'),
    # 我的推荐
    path('commend/', MycommendView.as_view(), name="my_commend"),
    # 常见问题
    path('problems/', MyproblemsView.as_view(), name="my_problems"),
    # 关于我们
    path('aboutus/', AboutusView.as_view(), name="aboutus"),

]


