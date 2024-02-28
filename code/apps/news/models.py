from django.db import models

# Create your models here.
#
#
#
# class AdvertisePartTime(models.Model):
#     #itemid = models.ForeignKey('Board', models.DO_NOTHING, db_column='ItemID', primary_key=True)  # Field name made lowercase.
#     #itemid = models.ForeignKey('Board', models.DO_NOTHING, db_column='ItemID')  # Field name made lowercase.
#     userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
#     mark = models.CharField(db_column='Mark', max_length=9)  # Field name made lowercase.
#     company = models.TextField()
#     releasetime = models.DateTimeField(db_column='ReleaseTime')  # Field name made lowercase.
#     details = models.CharField(max_length=1000, blank=True, null=True)
#     reward = models.IntegerField(blank=True, null=True)
#     contact = models.CharField(max_length=50)
#     time = models.DateField()
#     place = models.CharField(max_length=80)
#     #def __str__(self):
#         #return '<%s>  %s' % (self.get_asset_type_display(), self.name)
#
#     class Meta:
#         #managed = False
#         db_table = 'advertise_part-time'
#         #unique_together = (('itemid', 'userid'),)
#         unique_together = (('userid'),)
#
#
# class User(models.Model):
#     userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         #managed = False
#         db_table = 'user'
#         unique_together = (('id', 'userid'),)
#
#
#
#
#
# #class Board(models.Model):
#     #itemid = models.IntegerField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
#     #board = models.CharField(max_length=12, blank=True, null=True)
#
#     #class Meta:
#         #managed = False
#         #db_table = 'board'
#
#
#
#
# class Saleandbuy(models.Model):
#     #itemid = models.ForeignKey(Board, models.DO_NOTHING, db_column='ItemID', primary_key=True)  # Field name made lowercase.
#     #itemid = models.ForeignKey(Board, models.DO_NOTHING, db_column='ItemID')
#     userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
#     mark = models.CharField(db_column='Mark', max_length=14)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=19, blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
#     price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
#     detail = models.CharField(db_column='Detail', max_length=255, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         #managed = False
#         db_table = 'saleandbuy'
#        # unique_together = (('itemid', 'userid'),)
#         unique_together = (('userid'),)
#
#
# class SeekHelp(models.Model):
#     #itemid = models.ForeignKey(Board, models.DO_NOTHING, db_column='ItemID', primary_key=True)  # Field name made lowercase.
#     #itemid = models.ForeignKey(Board, models.DO_NOTHING, db_column='ItemID')
#     userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
#     mark = models.CharField(db_column='Mark', max_length=6)  # Field name made lowercase.
#     type = models.CharField(db_column='Type', max_length=15)  # Field name made lowercase.
#     releasetime = models.DateTimeField(db_column='ReleaseTime')  # Field name made lowercase.
#     details = models.CharField(max_length=1000, blank=True, null=True)
#     reward = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         #managed = False
#         db_table = 'seek_help'
#         #unique_together = (('itemid', 'userid'),)
#         unique_together = (('userid'),)

class TestScrapy(models.Model):
    title = models.CharField(max_length=255) #爬取通知的标题
    text = models.TextField()                  # 爬取通知的内容
    source = models.CharField(max_length=30)  # 爬取通知的来源页
    time = models.CharField (max_length=30) # 爬取通知的日期

    class Meta:
        app_label = 'news'
        db_table = 'test_scrapy'

class Xuegongnews(models.Model):
    title = models.CharField(max_length=255) #爬取通知的标题
    text = models.TextField()                  # 爬取通知的内容
    source = models.CharField(max_length=255)  # 爬取通知的来源页
    time = models.CharField (max_length=255) # 爬取通知的日期

    class Meta:
        app_label = 'news'
        db_table = 'xuegong_news'

class Qingchunnews(models.Model):
    title = models.CharField(max_length=255) #爬取通知的标题
    text = models.TextField()                  # 爬取通知的内容
    source = models.CharField(max_length=255)  # 爬取通知的来源页
    time = models.CharField (max_length=255) # 爬取通知的日期

    class Meta:
        app_label = 'news'
        db_table = 'qingchun_news'


class ContactPost(models.Model):
    # 姓名。models.CharField 为字符串字段，用于保存较短的字符串，比如姓名
    name = models.CharField(max_length=100)
    # email。
    email = models.CharField(max_length=100)
    # 所属院系。
    faculty = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列，即最新的数据永远显示在上部
        #ordering = ('-created',)
        app_label = 'news'
        db_table = 'Contact'
        # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容

    def __str__(self):
        # return self.title 将姓名返回
        return self.name