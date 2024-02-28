from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from news import models
from .forms import ContactPostForm
from lostfound.models import LostfoundPost
from ad.models import AdPost
from salebuy.models import SalebuyPost
from seekhelp.models import SeekhelpPost
from users.models import UserProfile
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View


# Create your views here.
def adv(request):
    advs = AdPost.objects.all()
    return render(request, 'news/adv.html', locals())


def lost(request):
    losts = LostfoundPost.objects.all()
    return render(request, 'news/lost.html', locals())


def sale(request):
    sales = SalebuyPost.objects.all()
    return render(request, 'news/sale.html', locals())


def seek(request):
    seeks = SeekhelpPost.objects.all()
    return render(request, 'news/seek.html', locals())



def inform(request):  # 定义通知类
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    informs = models.TestScrapy.objects.all()
    return render(request, 'news/inform.html', locals())


def inform_detail(request, inform_id):  # 定义通知详情页
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    inform = get_object_or_404(models.TestScrapy, id=inform_id)
    return render(request, 'news/inform_detail.html', locals())




def xiaoche(request):  # 定义校车页
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    return render(request, 'news/inform_service/xiaoche.html', locals())


def zxsj(request):  # 定义作息时间页
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    return render(request, 'news/inform_service/zxsj.html', locals())


def xiaoli(request):  # 定义校历页
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    return render(request, 'news/inform_service/xiaoli.html', locals())


def xuegong(request):  # 定义学工通知类
    xuegongs = models.Xuegongnews.objects.all()
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    return render(request, 'news/xuegong.html', locals())


def xuegong_detail(request, xuegong_id):  # 定义学工通知详情页
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    xuegong = get_object_or_404(models.Xuegongnews, id=xuegong_id)
    return render(request, 'news/xuegong_detail.html', locals())


def qingchun(request):  # 定义青春川大通知类
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    qingchuns = models.Qingchunnews.objects.all()
    return render(request, 'news/qingchun.html', locals())


def qingchun_detail(request, qingchun_id):  # 定义青春川大通知详情页
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    qingchun = get_object_or_404(models.Qingchunnews, id=qingchun_id)
    return render(request, 'news/qingchun_detail.html', locals())

def daily(request):
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    contacts = models.ContactPost.objects.all()
    return render(request, 'news/daily.html',locals())

def contact_create(request): #通讯录添加处0
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        contact_post_form = ContactPostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if contact_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_contact = contact_post_form.save(commit=False)
            # 将新文章保存到数据库中
            new_contact.save()
            # 完成后返回到文章列表
            return redirect("news:contact_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        contact_post_form = ContactPostForm()
        # 赋值上下文
        context = { 'contact_post_form': contact_post_form }
        # 返回模板
        return render(request, 'news/contact_create.html', context)


def dashboard(request):
    user = request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
    lostfound = LostfoundPost.objects.count()
    salebuy = SalebuyPost.objects.count()
    seekhelp = SeekhelpPost.objects.count()
    advpart = AdPost.objects.count()
    jiaowu = models.TestScrapy.objects.count()
    xuegong = models.Xuegongnews.objects.count()
    qingchun =models.Qingchunnews.objects.count()
    lost_rate = round(lostfound / (lostfound + salebuy + seekhelp + advpart) * 100)
    sale_rate = round(salebuy / (lostfound + salebuy + seekhelp + advpart) * 100)
    seek_rate = round(seekhelp / (lostfound + salebuy + seekhelp + advpart) * 100)
    adv_rate = round(advpart / (lostfound + salebuy + seekhelp + advpart) * 100)
    return render(request, 'news/dashboard.html', locals())




def user_inform(request):
    user=request.user
    if user is not None:
        user_informs = UserProfile.objects.filter(username=user)
        return render(request,'news/user.html',locals())

