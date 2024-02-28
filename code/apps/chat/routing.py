from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:chat_group_name>/', consumers.ChatConsumer),
]
