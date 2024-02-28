from django.db import models
# timezone 用于处理时间相关事务。
from django.utils import timezone
# 用户的表
from users.models import UserProfile


class Img(models.Model):
    img_url = models.ImageField(upload_to='img')


class SeekhelpPost(models.Model):
    # 帖子创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 帖子更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
    # 帖子作者，自动读取作者
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # 帖子标题，比较短，显示在首页
    title = models.CharField(max_length=100)
    # 详细描述，详细页面才显示，自己添加
    details = models.TextField(blank=True)

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列，即最新的数据永远显示在上部
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将帖子标题返回
        return self.title

