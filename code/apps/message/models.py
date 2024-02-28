from django.db import models
from users.models import UserProfile

# Create your models here.
class Msg(models.Model):
    # 设置一个自动增长的id
    id = models.AutoField(primary_key=True)
    #存取留言标题
    title = models.CharField(max_length=30)
    #存取留言内容
    content = models.TextField()
    #存取留言用户的id信息
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # 用于存取留言时间。 其中， auto_now_add 参数
    # 表示在建立一个新的 Msg 数据模型对象时，
    # 自动设置该属性值为当前时间。
    datetime = models.DateTimeField(auto_now_add=True)
    # 用于存取留言的点击次数信息。
    clickcount = models.IntegerField(default=0)
    email = models.EmailField(verbose_name='邮箱', null=False, blank=True, default="")

    # 内部类 class Meta 用于给 model 定义元数据
    # 元数据：不是一个字段的任何数据
    class Meta:
        verbose_name = '留言板内容'
        ordering = ['-datetime']  # 按 name 字段排序，默认为升序，`-`表示倒序，`?`表示随机
        db_table = "msg"  # 该类对应数据库表名

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    # 它最常见的就是在Django管理后台中做为对象的显示值。因此应该总是为 __str__ 返回一个友好易读的字符串
    def __str__(self):
        # return self.title 将留言标题返回
        return self.title
