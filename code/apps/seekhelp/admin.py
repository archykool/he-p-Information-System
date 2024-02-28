from django.contrib import admin

# 别忘了导入SeekhelpPost
from .models import SeekhelpPost

# 注册SeekhelpPost到admin中
admin.site.register(SeekhelpPost)