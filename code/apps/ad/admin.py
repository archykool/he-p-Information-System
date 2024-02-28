from django.contrib import admin

# 别忘了导入AdPost
from .models import AdPost

# 注册AdPost到admin中
admin.site.register(AdPost)