from django.urls import path
from django.contrib import admin


from . import views
from .api import views as api_views

app_name = 'chat'

urlpatterns = [
    path('allfriends/', views.allchats, name='allfriends'),
    path('allfriends/<int:group_id>', api_views.ListChats.as_view(), name='get-chat_groups-api'),
    path('admin/', admin.site.urls),

]