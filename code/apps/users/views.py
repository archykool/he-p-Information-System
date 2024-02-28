# users/views.py
import json

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from ad.forms import AdPostForm
from ad.models import AdPost
from lostfound.forms import LostfoundPostForm
from lostfound.models import LostfoundPost
from salebuy.forms import SalebuyPostForm
from salebuy.models import SalebuyPost
from seekhelp.forms import SeekhelpPostForm
from seekhelp.models import SeekhelpPost
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_eamil
from utils.mixin_utils import LoginRequiredMixin
from .forms import UploadImageForm, UserInfoForm
from django.urls import reverse
# 导入分页用的包
from django.core.paginator import Paginator


# 邮箱和用户名都可以登录
# 基与ModelBackend类，因为它有authenticate方法
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 登录
class LoginView(View):
    '''用户登录'''

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)
            # 如果不是null说明验证成功
            if user is not None:
                if user.is_active:
                    # 只有注册激活才能登录
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
            # 只有当用户名或密码不存在时，才返回错误信息到前端
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})

        # form.is_valid（）已经判断不合法了，所以这里不需要再返回错误信息到前端了
        else:
            return render(request, 'login.html', {'login_form': login_form})


# 激活用户
class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code=active_code)

        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 查找到邮箱对应的user
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        # 验证码不对的时候跳转到激活失败页面
        else:
            return render(request, 'user/active_fail.html')
        # 激活成功跳转到登录页面
        return render(request, "login.html", )


class LogoutView(View):
    '''用户登出'''

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


# 注册
class RegisterView(View):
    '''用户注册'''

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', None)
            # 如果用户已存在，则提示错误信息
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已存在'})

            pass_word = request.POST.get('password', None)
            # 实例化一个user_profile对象
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            # 对保存到数据库的密码加密
            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_eamil(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ForgetPwdView(View):
    '''找回密码'''

    def get(self, request):
        forget_form = ForgetPwdForm()
        return render(request, 'user/forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', None)
            send_register_eamil(email, 'forget')
            return render(request, 'user/send_success.html')
        else:
            return render(request, 'user/forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "user/password_reset.html", {"email": email})
        else:
            return render(request, "user/active_fail.html")
        return render(request, "login.html")


class ModifyPwdView(View):
    '''修改用户密码'''

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "user/password_reset.html", {"email": email, "msg": "密码不一致！"})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "user/password_reset.html", {"email": email, "modify_form": modify_form})


class UserinfoView(LoginRequiredMixin, View):
    """
    用户个人信息
    """

    def get(self, request):
        return render(request, 'user/info.html', {})

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class UploadImageView(LoginRequiredMixin, View):
    '''用户图像修改'''

    def post(self, request):
        # 上传的文件都在request.FILES里面获取，所以这里要多传一个这个参数
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.cleaned_data['image']
            request.user.image = image
            request.user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail"}', content_type='application/json')


class UpdatePwdView(View):
    """
    个人中心修改用户密码
    """

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            if pwd1 != pwd2:
                return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type='application/json')
            user = request.user
            user.password = make_password(pwd2)
            user.save()

            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')


class SendEmailCodeView(LoginRequiredMixin, View):
    '''发送邮箱修改验证码'''

    def get(self, request):
        email = request.GET.get('email', '')

        if UserProfile.objects.filter(email=email):
            return HttpResponse('{"email":"邮箱已存在"}', content_type='application/json')

        send_register_eamil(email, 'update_email')
        return HttpResponse('{"status":"success"}', content_type='application/json')


class UpdateEmailView(LoginRequiredMixin, View):
    '''修改邮箱'''

    def post(self, request):
        email = request.POST.get("email", "")
        code = request.POST.get("code", "")

        existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email')
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"email":"验证码无效"}', content_type='application/json')



class MycommendView(LoginRequiredMixin, View):
    '''我的推荐'''

    def get(self, request):
        return render(request, "user/commend.html", )


class MyproblemsView(LoginRequiredMixin, View):
    '''常见问题'''

    def get(self, request):
        return render(request, "user/problems.html", )


class AboutusView(LoginRequiredMixin, View):
    '''常见问题'''
    def get(self, request):
        return render(request, "user/aboutus.html", )


def ad_list(request):
    author = request.user
    ads = AdPost.objects.filter(author=author)
    context = {'ads': ads}
    return render(request, 'user/post_ad.html', context)


def lostfound_list(request):
    # 取出所有网站帖子
    author = request.user
    lostfounds = LostfoundPost.objects.filter(author=author)
    # 需要传递给模板（templates）的对象
    context = {'lostfounds': lostfounds}
    # render函数：载入模板，并返回context对象
    return render(request, 'user/post_lostfound.html', context)


def seekhelp_list(request):
    # 取出所有网站帖子
    author = request.user
    seekhelps = SeekhelpPost.objects.filter(author=author)
    # 需要传递给模板（templates）的对象
    context = {'seekhelps': seekhelps}
    # render函数：载入模板，并返回context对象
    return render(request, 'user/post_seekhelp.html', context)


def salebuy_list(request):
    # 取出所有网站帖子
    author = request.user
    salebuys = SalebuyPost.objects.filter(author=author)
    # 需要传递给模板（templates）的对象
    context = {'salebuys': salebuys}
    # render函数：载入模板，并返回context对象
    return render(request, 'user/post_salebuy.html', context)


# 修改帖子
def ad_update(request, id):
    # 获取需要修改的具体帖子对象
    ad = AdPost.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        ad_post_form = AdPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if ad_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            ad.title = request.POST['title']
            ad.price = request.POST['price']
            ad.details = request.POST['details']
            ad.save()
            return redirect("users:mypost_ad")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        ad_post_form = AdPostForm()
        # 赋值上下文，将 ad 帖子对象也传递进去，以便提取旧的内容
        context = {'ad': ad, 'ad_post_form': ad_post_form}
        # 将响应返回到模板中
        return render(request, 'user/update_ad.html', context)


def lostfound_update(request, id):
    # 获取需要修改的具体帖子对象
    lostfound = LostfoundPost.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        lostfound_post_form = LostfoundPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if lostfound_post_form.is_valid():
            # 保存新写入的 title、details 数据并保存
            lostfound.title = request.POST['title']
            lostfound.type = request.POST['type']
            lostfound.location = request.POST['location']
            lostfound.address = request.POST['address']
            lostfound.objecttime = request.POST['objecttime']
            lostfound.details = request.POST['details']
            lostfound.save()
            return redirect("users:mypost_lostfound")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        lostfound_post_form = LostfoundPostForm()
        # 赋值上下文，将 topic 帖子对象也传递进去，以便提取旧的内容
        context = {'lostfound': lostfound, 'lostfound_post_form': lostfound_post_form}
        # 将响应返回到模板中
        return render(request, 'user/update_lostfound.html', context)


def salebuy_update(request, id):
    # 获取需要修改的具体帖子对象
    salebuy = SalebuyPost.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        salebuy_post_form = SalebuyPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if salebuy_post_form.is_valid():
            salebuy.title = request.POST['title']
            salebuy.type = request.POST['type']
            salebuy.location = request.POST['location']
            salebuy.price = request.POST['price']
            salebuy.details = request.POST['details']
            salebuy.save()
            return redirect("users:mypost_salebuy")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        salebuy_post_form = SalebuyPostForm()
        # 赋值上下文，将 salebuy 帖子对象也传递进去，以便提取旧的内容
        context = { 'salebuy': salebuy, 'salebuy_post_form': salebuy_post_form }
        # 将响应返回到模板中
        return render(request, 'user/update_salebuy.html', context)


def seekhelp_update(request, id):
    # 获取需要修改的具体帖子对象
    seekhelp = SeekhelpPost.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        seekhelp_post_form = SeekhelpPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if seekhelp_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            seekhelp.title = request.POST['title']
            seekhelp.details = request.POST['details']
            seekhelp.save()
            return redirect("users:mypost_seekhelp")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        seekhelp_post_form = SeekhelpPostForm()
        # 赋值上下文，将 seekhelp 帖子对象也传递进去，以便提取旧的内容
        context = { 'seekhelp': seekhelp, 'seekhelp_post_form': seekhelp_post_form }
        # 将响应返回到模板中
        return render(request, 'user/update_seekhelp.html', context)


# 删除帖子
def seekhelp_delete(request, id):
    # 根据 id 获取需要删除的帖子
    seekhelp = SeekhelpPost.objects.get(id=id)
    # 调用.delete()方法删除帖子
    seekhelp.delete()
    # 完成删除后返回帖子列表
    return redirect("users:mypost_seekhelp")


# 删除帖子
def salebuy_delete(request, id):
    # 根据 id 获取需要删除的帖子
    salebuy = SalebuyPost.objects.get(id=id)
    # 调用.delete()方法删除帖子
    salebuy.delete()
    # 完成删除后返回帖子列表
    return redirect("users:mypost_salebuy")


# 删除帖子
def ad_delete(request, id):
    # 根据 id 获取需要删除的帖子
    ad = AdPost.objects.get(id=id)
    # 调用.delete()方法删除帖子
    ad.delete()
    # 完成删除后返回帖子列表
    return redirect("users:mypost_ad")


# 删除帖子
def lostfound_delete(request, id):
    # 根据 id 获取需要删除的帖子
    lostfound = LostfoundPost.objects.get(id=id)
    # 调用.delete()方法删除帖子
    lostfound.delete()
    # 完成删除后返回帖子列表
    return redirect("users:mypost_lostfound")


class IndexView(View):
    """首页"""

    def get(self, request):
        return render(request, 'index.html', )


def page_not_found(request, exception):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response


