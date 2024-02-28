from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Msg
from message.forms import MsgPostForm
from users.models import UserProfile
# 导入分页用的包
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, 'message/msg_index.html')


def showAll(request):
    allInfo = Msg.objects.all()
    paginator = Paginator(allInfo, 5)
    page = request.GET.get('page')
    msgs = paginator.get_page(page)
    context = {'msgs': msgs}
    return render(request, 'message/msg_showAll.html', locals())


# 留言详情
def message_detail(request, id):
    message = get_object_or_404(Msg, id=id)
    return render(request, 'message/msg_detail.html', {'message':message})


# 写留言
@login_required
def msg_post_page(request):
    if request.method=='POST':
        form =MsgPostForm(data=request.POST)
        if form.is_valid():
            user = request.user
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')
            newmessage = Msg()
            newmessage.user = user
            newmessage.title = title
            newmessage.content = content
            newmessage.save()
            return render(request, 'message/msg_succeed.html')
    else:
        form = MsgPostForm()
        context = {'form':form}
        return render(request, 'message/msg_add.html', context)

def succeed(request):
    return render(request, 'message/msg_succeed.html')

def user_msg_list_page(request, username):
    #需要用get_object_or_404返回能够被Msg使用的参数。
    user = get_object_or_404(UserProfile, username=username)
    #查找符合条件的记录集
    user_msgs = Msg.objects.filter(user=user)
    context ={'user_msgs':user_msgs}
    return render(request, 'message/user_msg_list_page.html', context)

def my_msg_list_page(request):
    user = request.user
    my_msgs = Msg.objects.filter(user=user)
    context = {'my_msgs':my_msgs}
    return render(request, 'message/my_msg_list_page.html', context)

