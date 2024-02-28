# 引入表单类
from django import forms
# 引入帖子模型
from .models import SalebuyPost


# 写帖子的表单类
class SalebuyPostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = SalebuyPost
        # 定义表单包含的字段
        fields = ('title', 'type', 'location', 'price', 'details')
