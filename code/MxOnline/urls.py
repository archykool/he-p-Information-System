# MxOnline/urls.py


from django.urls import path,re_path

from django.views.generic import TemplateView

from users import views
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, IndexView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
from users.views import LogoutView
from django.conf.urls import url
from django.conf.urls import include
from django.views.generic import RedirectView





urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),


    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),


    # 个人信息
    path("users/", include('users.urls', namespace="users")),

    # 富文本相关url

    path('ad/', include('ad.urls', namespace='ad')),
    path('lostfound/', include('lostfound.urls', namespace='lostfound')),
    path('salebuy/', include('salebuy.urls', namespace='salebuy')),
    path('seekhelp/', include('seekhelp.urls', namespace='seekhelp')),
    url(r'^news/', include('news.urls')),  # 金卓扬增加的部分
    # 消息中心
    path('message/', include('message.urls', namespace='message')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('sys_msg/', include('systermmsg.urls', namespace='systermmsg')),
]

# 全局404页面配置
handler404 = 'users.views.page_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'