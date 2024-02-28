from django.db import models
from users.models import UserProfile
from django.utils import timezone

# Create your models here.
class chat_group(models.Model):
    #聊天组的名称，由两个用户名组成
    name = models.CharField(max_length=30)
    #更新时间，如果消息不为空，以最后一条消息为准
    #如果消息为空，则为创建时间
    updated_at = models.DateTimeField()
    members = models.ManyToManyField(UserProfile,related_name='usergroup')

    def __str__(self):
        return self.name



class chat_msgs(models.Model):
    #显示是哪个组的消息
    group = models.ForeignKey(chat_group, on_delete=models.CASCADE)
    #显示是哪个用户发的消息
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #文本信息
    text_msg = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

# class user_group(models.Model):
#     #用户拥有的聊天组
#     id = models.AutoField(primary_key=True)
#     #用户的id
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     #聊天组的id
#     group = models.ForeignKey(chat_group, on_delete=models.CASCADE)
#     #创建的时间
#     created_at = models.DateTimeField(auto_now_add=True)
#
