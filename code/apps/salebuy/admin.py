from django.contrib import admin

# 别忘了导入SalebuyPost
from .models import SalebuyPost

# 注册SalebuyPost到admin中
admin.site.register(SalebuyPost)