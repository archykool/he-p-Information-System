from django.contrib import admin

# Register your models here.
from .models import chat_msgs, chat_group

@admin.register(chat_group)
class chat_groupAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated_at')

@admin.register(chat_msgs)
class chat_msgsAdmin(admin.ModelAdmin ):
    list_display = ('user','group','text_msg','created_at')