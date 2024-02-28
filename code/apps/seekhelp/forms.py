# 引入表单类
from django import forms
# 引入帖子模型
from .models import SeekhelpPost


# 写帖子的表单类
class SeekhelpPostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = SeekhelpPost
        # 定义表单包含的字段
        fields = ('title', 'details')
