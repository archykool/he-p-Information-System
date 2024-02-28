from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LostfoundPostForm
from .models import LostfoundPost, Img
from ad.models import AdPost
from salebuy.models import SalebuyPost
from seekhelp.models import SeekhelpPost
# 导入分页用的包
from django.core.paginator import Paginator
# 登录检查
from django.contrib.auth.decorators import login_required


# 查看所有的帖子
def lostfound_list(request):
    # 取出所有网站帖子
    lost_list = LostfoundPost.objects.all()
    paginator = Paginator(lost_list, 5)
    page = request.GET.get('page')
    losts = paginator.get_page(page)
    context = {'losts': losts}
    return render(request, 'lostfound/list.html', locals())


# 查看帖子详情
def lostfound_detail(request, id):
    lostfounds = LostfoundPost.objects.all()
    conlost = {'lostfounds': lostfounds}
    salebuys = SalebuyPost.objects.all()
    consale = {'salebuys': salebuys}
    ads = AdPost.objects.all()
    conad = {'ads': ads}
    seekhelps = SeekhelpPost.objects.all()
    conseek = {'seekhelps': seekhelps}
    lostfound = LostfoundPost.objects.get(id=id)
    img = Img.objects.get(id=id)
    context = {'lostfound': img}
    content_type = {'lostfound': lostfound }
    return render(request, 'lostfound/detail.html', locals())


@login_required
# 写帖子的视图
def lostfound_create(request):
    lostfounds = LostfoundPost.objects.all()
    conlost = {'lostfounds': lostfounds}
    salebuys = SalebuyPost.objects.all()
    consale = {'salebuys': salebuys}
    ads = AdPost.objects.all()
    conad = {'ads': ads}
    seekhelps = SeekhelpPost.objects.all()
    conseek = {'seekhelps': seekhelps}
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        lostfound_post_form = LostfoundPostForm(data=request.POST)
        # 添加图片
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        # 判断提交的数据是否满足模型的要求
        if lostfound_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_lostfound = lostfound_post_form.save(commit=False)
            # 指定当前用户为作者
            new_lostfound.author = request.user
            # 将新文章保存到数据库中
            new_lostfound.save()
            # 完成后返回到文章列表
            return redirect("lostfound:lostfound_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单中有数据不合法")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        lostfound_post_form = LostfoundPostForm()
        # 赋值上下文
        context = {'lostfound_post_form': lostfound_post_form}
        # 返回模板
        return render(request, 'lostfound/create.html', locals())


# 删除帖子
def lostfound_delete(request, id):
    # 根据 id 获取需要删除的帖子
    lostfound = LostfoundPost.objects.get(id=id)
    # 调用.delete()方法删除帖子
    lostfound.delete()
    # 完成删除后返回帖子列表
    return redirect("lostfound:lostfound_list")


# 修改帖子
def lostfound_update(request, id):
    """
    修改帖子的视图函数
    通过POST方法提交表单，更新titile、body字段
    GET方法进入初始表单页面
    id： 帖子的 id
    """

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
            lostfound.details = request.POST['location']
            lostfound.details = request.POST['details']
            lostfound.save()
            # 完成后返回到修改后的帖子中。需传入帖子的 id 值
            return redirect("lostfound:lostfound_detail", id=id)
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
        return render(request, 'lostfound/update.html', context)
