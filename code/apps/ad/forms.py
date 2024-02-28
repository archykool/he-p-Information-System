# 引入表单类
from django import forms
# 引入帖子模型
from .models import AdPost


# 写帖子的表单类
class AdPostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = AdPost
        # 定义表单包含的字段
        fields = ('title', 'price', 'details')
