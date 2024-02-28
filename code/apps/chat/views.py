from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from users.models import UserProfile
from django.db.models import Q
from chat.models import *


@login_required
def allchats(request):
    if not request.user.is_authenticated:
        redirect('login')
    #获取当前用户
    user = UserProfile.objects.get(id=request.user.id)
        #获取当前用户的所有聊天
    allchats = user.usergroup.filter(members= user)
    #获取每个聊天中的另一个用户
    allfriends = UserProfile.objects.none()
    for chat in allchats:
        friend = chat.members.filter(usergroup=chat.id).exclude(id=user.id)
        allfriends = allfriends | friend



    context = {
         'allchats': allchats,
         'allfriends': allfriends
    }
    return render(request, 'chat/chat_base.html', context)

# def creategroup(request,username):
#     #获取当前用户
#     user = request.user
#     #获取其他用户
#     otheruser = UserProfile.objects.get(username=username)
#     #获取其他用户所在的聊天
#     otheruser_group = otheruser.usergroup.filter(members=otheruser)
#     group = otheruser_group.get(members__in=user)
#     if group==None:
#         str = user.username + '&' + otheruser.username
#         newgroup = chat_group(name=str)
#         newgroup.save()
#         newgroup = chat_group.objects.get(name=str)
#         newgroup.members.add(user)
#         newgroup.members.add(otheruser)
#         newgroup.save()
#         return render(request, 'chat/chat_base.html')
#     else:
#         return render(request, 'chat/chat_base.html')