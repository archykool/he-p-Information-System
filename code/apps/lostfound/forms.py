# 引入表单类
from django import forms
# 引入帖子模型
from .models import LostfoundPost


# 写帖子的表单类
class LostfoundPostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = LostfoundPost
        # 定义表单包含的字段
        fields = ('title', 'type', 'location', 'address', 'objecttime', 'details')
