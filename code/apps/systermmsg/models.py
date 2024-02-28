from django.db import models

# Create your models here.
class SystermMsg(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    abstract = models.TextField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        # return self.title 将留言标题返回
        return self.title
