from django.contrib import admin

# 别忘了导入LostfoundPost
from .models import LostfoundPost

# 注册LostfoundPost到admin中
admin.site.register(LostfoundPost)
