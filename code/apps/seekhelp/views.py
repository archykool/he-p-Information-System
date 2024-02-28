# 引入redirect重定向模块
from django.shortcuts import render, redirect
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的SeekhelpPostForm表单类
from .forms import SeekhelpPostForm
# 导入数据模型SeekhelpPost
from .models import SeekhelpPost, Img
from lostfound.models import LostfoundPost
from salebuy.models import SalebuyPost
from ad.models import AdPost
# 导入分页所用的包
from django.core.paginator import Paginator
# 登录检查
from django.contrib.auth.decorators import login_required


# 查看所有的帖子
def seekhelp_list(request):
    # 取出所有网站帖子
    seek_list = SeekhelpPost.objects.all()
    paginator = Paginator(seek_list, 5)
    page = request.GET.get('page')
    seeks = paginator.get_page(page)
    context = {'seeks': seeks}
    return render(request, 'seekhelp/list.html', locals())


# 查看帖子详情
def seekhelp_detail(request, id):
    lostfounds = LostfoundPost.objects.all()
    conlost = {'lostfounds': lostfounds}
    salebuys = SalebuyPost.objects.all()
    consale = {'salebuys': salebuys}
    ads = AdPost.objects.all()
    conad = {'ads': ads}
    seekhelps = SeekhelpPost.objects.all()
    conseek = {'seekhelps': seekhelps}
    seekhelp = SeekhelpPost.objects.get(id=id)
    img = Img.objects.get(id=id)
    context = {'seekhelp': img}
    content_type = {'seekhelp': seekhelp }
    return render(request, 'seekhelp/detail.html', locals())


@login_required
# 写帖子的视图
def seekhelp_create(request):
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
        seekhelp_post_form = SeekhelpPostForm(data=request.POST)
        # 添加图片
        img = Img(img_url=request.FILES.get('img'))
        img.save()
        # 判断提交的数据是否满足模型的要求
        if seekhelp_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_seekhelp = seekhelp_post_form.save(commit=False)
            # 指定当前用户为作者
            new_seekhelp.author = request.user
            # 将新文章保存到数据库中
            new_seekhelp.save()
            # 完成后返回到文章列表
            return redirect("seekhelp:seekhelp_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        seekhelp_post_form = SeekhelpPostForm()
        # 赋值上下文
        context = { 'seekhelp_post_form': seekhelp_post_form }
        # 返回模板
        return render(request, 'seekhelp/create.html', locals())


# 修改帖子
def seekhelp_update(request, id):
    """
    修改帖子的视图函数
    通过POST方法提交表单，更新titile、body字段
    GET方法进入初始表单页面
    id： 帖子的 id
    """

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
            seekhelp.body = request.POST['body']
            seekhelp.save()
            # 完成后返回到修改后的帖子中。需传入帖子的 id 值
            return redirect("seekhelp:seekhelp_detail", id=id)
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
        return render(request, 'seekhelp/update.html', context)

